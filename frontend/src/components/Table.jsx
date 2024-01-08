import React, { useEffect, useState} from 'react';
import axios from 'axios';
import './style.css';
import 'bootstrap/dist/css/bootstrap.min.css';


const Table = ({ labels, data }) => {
  return (
    <div className="container mt-5 d-flex justify-content-center table-container">
      <table className="terminal" id="appendable">
        <thead>
          <tr className="terminal-row">
            {labels.map((label) => (
              <th className="terminal-cell" key={label}>
                <p>{label}</p>
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {data.map((rowData, rowIndex) => (
            <tr className="terminal-row" key={rowIndex}>
              {labels.map((label) => (
                <td className="terminal-cell" key={label}>
                  <p>{rowData[label]}</p>
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Table;