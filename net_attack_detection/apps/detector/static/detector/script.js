document.getElementById('predict-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    console.log("HEY")
    const ipv4src = document.getElementById('ipv4_src_addr').value;
    const l4srcport = document.getElementById('l4_src_port').value;
    const ipv4dst = document.getElementById('ipv4_dst_addr').value;
    const l4dstport = document.getElementById('l4_dst_port').value;
    const protocol = document.getElementById('protocol').value;
    const l7proto = document.getElementById('l7_proto').value;
    const inbytes = document.getElementById('in_bytes').value;
    const outbytes = document.getElementById('out_bytes').value;
    const inpkts = document.getElementById('in_pkts').value;
    const outpkts = document.getElementById('out_pkts').value;
    const tcpflags = document.getElementById('tcp_flags').value;
    const flowdur = document.getElementById('flow_duration').value;

    const formData = {
        'IPV4_SRC_ADDR': ipv4src,
        'L4_SRC_PORT': l4srcport,
        'IPV4_DST_ADDR': ipv4dst,
        'L4_DST_PORT': l4dstport,
        'PROTOCOL': protocol,
        'L7_PROTO': l7proto,
        'IN_BYTES': inbytes,
        'OUT_BYTES': outbytes,
        'IN_PKTS': inpkts,
        'OUT_PKTS': outpkts,
        'TCP_FLAGS': tcpflags,
        'FLOW_DURATION_MILLISECONDS': flowdur
    };

    
    const response = await fetch('/predict/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: {'data':JSON.stringify(formData)}
    });
 
    if (response.ok) {
        const result = await response.json();
        document.getElementById('prediction-result').innerText = `Prediction: ${result.prediction}`;
    } else {
        document.getElementById('prediction-result').innerText = 'Error: Failed to predict';
    }
}); 


