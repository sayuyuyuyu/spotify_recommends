import React, { useState, useCallback } from 'react';
import './EmotionMap.css';

const EmotionMap = () => {
  const [isDragging, setIsDragging] = useState(false);
  const [position, setPosition] = useState({ x: 150, y: 150 }); // 初期位置

  const handleMouseDown = useCallback((event) => {
    setIsDragging(true);
  }, []);

  const handleMouseMove = useCallback(
    (event) => {
      if (isDragging) {
        const map = event.target.closest("#emotion-map");
        const rect = map.getBoundingClientRect();
        const x = event.clientX - rect.left;
        const y = event.clientY - rect.top;
        // グラフのサイズ内に収まるように制限
        if (x >= 0 && x <= rect.width && y >= 0 && y <= rect.height) {
          setPosition({ x, y });
        }
      }
    },
    [isDragging]
  );

  const handleMouseUp = useCallback(() => {
    setIsDragging(false);
    // ここで位置情報を使用するロジックを追加できます
  }, []);

  return (
    <div
      id="emotion-map"
      onMouseMove={handleMouseMove}
      onMouseLeave={handleMouseUp} // マウスが領域外に出たときにドラッグを解除
      onMouseUp={handleMouseUp}
      style={{ width: '500px', height: '300px', position: 'relative', border: '1px solid black' }}
    >
      <div
        id="point"
        onMouseDown={handleMouseDown}
        style={{
          position: 'absolute',
          width: '20px',
          height: '20px',
          backgroundColor: 'red',
          borderRadius: '50%',
          cursor: 'pointer',
          left: `${position.x}px`,
          top: `${position.y}px`,
          transform: 'translate(-50%, -50%)',
        }}
      />
    </div>
  );
};

export default EmotionMap;