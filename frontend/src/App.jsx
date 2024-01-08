import React, { useState, useEffect, useRef } from 'react';
import Table from './components/Table';
import 'bootstrap/dist/css/bootstrap.min.css';
import'./style.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faCheck } from '@fortawesome/free-solid-svg-icons'
import { faXmark } from '@fortawesome/free-solid-svg-icons'

const App = () => {
  const btRef = useRef();
  const [labels, setLabels] = useState([]);
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchedLabels = ['IPV4_SRC_ADDR', 'L4_SRC_PORT', 'IPV4_DST_ADDR', 'L4_DST_PORT', 'PROTOCOL', 'L7_PROTO', 'IN_BYTES', 'OUT_BYTES', 'IN_PKTS', 'OUT_PKTS', 'TCP_FLAGS', 'FLOW_DURATION_MILLISECONDS', 'STATUS', 'COMMENT'];
    setLabels(fetchedLabels);
  }, []);

  const fetchData = async () => {
    try {
      for(let i=0;i<(5 + (Math.random() * (10)));i++){
      const response = await fetch("http://127.0.0.1:8000/get_data/");
      const result = await response.json();
      console.log(result);

      // Call predict API
      const predictResponse = await fetch("http://127.0.0.1:8000/predict/", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(result),
      });

      const predictResult = await predictResponse.json();
      console.log('Prediction result:', predictResult.prediction);

      // Check if prediction is greater than 0.5
      //#<td class="terminal-cell"><i class="fa fa-check benign"></i><i class="fa fa-check malicious"></i></td>
      const status = predictResult.prediction >= 0.5 ? <FontAwesomeIcon icon={faXmark} className="malicious"/> : <FontAwesomeIcon icon={faCheck} className="benign"/>;

      let comment = '';

      if (predictResult.prediction >= 0.5) {
        console.log(result)
        const diagnoseResponse = await fetch("http://127.0.0.1:8000/diagnose/", {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(result),
        });

        const diagnoseResult = await diagnoseResponse.json();
        console.log('Diagnosis result:', diagnoseResult);
        let com1 = diagnoseResult.prediction[0];
        let com2 = diagnoseResult.prediction[1];
        console.log(com1+" "+com2);
        if(com1 == com2){
          comment = "Possible attack: "+diagnoseResult.prediction[0];
        }
        else if(com1 == "Other Malicious Activities"){
          comment = "Possible attacks: " + "Reconnaissance, XSS, Backdoor or " + com2;
        }
        else if(com2 == "Other Malicious Activities"){
          comment = "Possible attacks: " + "Reconnaissance, XSS, Backdoor or " + com1;
        }
        else{
        comment = "Possible attacks: "+diagnoseResult.prediction[0]+" or "+diagnoseResult.prediction[1] ;
        }
      }

      // Write the full result, including the status value and comment value
      setData((prevData) => [...prevData, { ...result, STATUS: status, COMMENT: comment }]);
      btRef.current.scrollIntoView({behavior: 'smooth'})
    }
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  return (
    <div className="d-flex justify-content-center flex-column">
      <nav className="navbar navbar-expand-lg navbar-light bg-light">
        <a className="navbar-brand p-2" href="#">
          Network Attack Detection
        </a>
      </nav>
      <div class="scroller">
      <Table labels={labels} data={data} />
      <div class="flag" ref={btRef} />
      </div>
      <div className="btnholder mt-5 d-flex justify-content-center">
        <button className="btn btn-danger btngo" onClick={() => fetchData()}>
          Run the simulation!
        </button>
      </div>
    </div>
  );
};

export default App;