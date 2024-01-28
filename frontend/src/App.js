// src/App.js
import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';
import q1Image from './q1.png';
import q2Image from './q2.png';
import q3Image from './q3.png';
import q4Image from './q4.png';
import q5Image from './q5.png';




function HomePage({ onButtonClick }) {
  console.log('HomePage rendered!');
  return (
    <div>
      <h2>STEM SAGA</h2>
      <button className="App-button" onClick={onButtonClick}>
        Start
      </button>
    </div>
  );
}








function Question1({ onContinueClick }) {
  //const [score, setScore] = useState(0);
  const [selectedAnswer, setSelectedAnswer] = useState(null);
  const [userInput, setUserInput] = useState('');




  const answerOptions = ['A', 'B', 'C', 'D'];




  /*const increaseScore = () => {
    setScore(score + 1);
  };*/




  const handleAnswerClick = (answer) => {
    setSelectedAnswer(answer);
  };




  const handleInputChange = (event) => {
    setUserInput(event.target.value);
  };


  console.log('MiddlePage rendered!');
  const imageSize = {width: '400px', height: '400px',  marginBottom: '200px', marginLeft: '100px'};
 
  return (
    <div>
     
      <h2>Select An Image</h2>
      <img src = {q1Image}  alt="Image Description" style={imageSize}/>


       {/* First answer option */}
       <div
        className={`answer-box ${selectedAnswer === 'A' ? 'selected' : ''}`}
        onClick={() => handleAnswerClick('A')}
        style={{ position: 'absolute', top: '300px', left: '375px' }}
      >
        A
      </div>




      {/* Second answer option */}
      <div
        className={`answer-box ${selectedAnswer === 'B' ? 'selected' : ''}`}
        onClick={() => handleAnswerClick('B')}
        style={{ position: 'absolute', top: '300px', left: '850px' }}
      >
        B
      </div>




      {/* Third answer option */}
      <div
        className={`answer-box ${selectedAnswer === 'C' ? 'selected' : ''}`}
        onClick={() => handleAnswerClick('C')}
        style={{ position: 'absolute', top: '500px', left: '375px' }}
      >
        C
      </div>




      {/* Fourth answer option */}
      <div
        className={`answer-box ${selectedAnswer === 'D' ? 'selected' : ''}`}
        onClick={() => handleAnswerClick('D')}
        style={{ position: 'absolute', top: '500px', left: '850px' }}
      >
        D
      </div>
     
      <textarea
        className="text-input"
        placeholder="Type your answer here..."
        value={userInput}
        onChange={handleInputChange}
        style={{ position: 'absolute', top: '700px', left: '450px', width: '300px', lenght: '500px', height: '50px' }}
      />


      <button className="App-button" onClick={onContinueClick}>
        Continue
      </button>
    </div>
  );
}


function NewMiddlePage({ onContinueClick }) {
  const [userInput, setUserInput] = useState('');




  const handleInputChange = (event) => {
    setUserInput(event.target.value);
  };




  console.log('NewMiddlePage rendered!');
  return (
    <div>
      <h2>New Question</h2>
      <textarea
        className="text-input"
        placeholder="Type your question here..."
        value={userInput}
        onChange={handleInputChange}
      />
      <div className="answer-options">
        {/* You can add your answer boxes here */}
      </div>
      <button className="App-button" onClick={onContinueClick}>
        Continue
      </button>
    </div>
  );
}






function EndPage({ onBackToHomeClick }) {
  console.log('EndPage rendered!');
  return (
    <div>
      <h2>Congratulations! </h2>
      <p>Thanks for playing the game.</p>
      <button className="App-button" onClick={onBackToHomeClick}>
        Play Again
      </button>
    </div>
  );
}




function App() {
  const [currentPage, setCurrentPage] = useState('home');




  const handleButtonClick = () => {
    setCurrentPage('question1');
  };




  const handleContinueToNewMiddlePage = () => {
    setCurrentPage('newMiddle');
  };




  const handleContinueToNewEndPage = () => {
    setCurrentPage('newEnd');
  };




  const handleBackToHomeClick = () => {
    setCurrentPage('home');
  };




  return (
    <div className="App">
      <header className="App-header">
        <p></p>
        {currentPage === 'home' && (
          <HomePage onButtonClick={handleButtonClick} />
        )}
        {currentPage === 'question1' && (
          <Question1  onContinueClick={handleContinueToNewMiddlePage} />
        )}
        {currentPage === 'newMiddle' && (
          <NewMiddlePage onContinueClick={handleContinueToNewEndPage} />
        )}
        {currentPage === 'newEnd' && (
          <EndPage onBackToHomeClick={handleBackToHomeClick} />
        )}
      </header>
    </div>
  );
}




export default App;


