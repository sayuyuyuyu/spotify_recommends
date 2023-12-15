import React from 'react';
import './App.css';
import EmotionMap from './EmotionMap';

function App() {
  return (
    <div className="App">
      <div className="centered-content">
        <h1>何から探す？</h1>
        <div className="button-container">
          <SearchButton label="アーティストから" />
          <SearchButton label="曲名から" />
          <SearchButton label="ジャンルから" />
          <SearchButton label="今の気分から" />
        </div>
        <EmotionMap />
      </div>
    </div>
  );
}

function SearchButton({ label }) {
  return (
    <button className="search-button" onClick={() => alert(`${label}を探します`)}>
      {label}
    </button>
  );
}

export default App;