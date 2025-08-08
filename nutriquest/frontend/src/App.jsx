import React, { useState, useEffect } from 'react';
import './App.css';

const RESOURCE = 'food-items';

function App() {
  const [items, setItems] = useState([]);
  const [newItem, setNewItem] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Fetch list of food items on mount
  useEffect(() => {
    async function fetchItems() {
      const url = `/api/${RESOURCE}/`;
      console.log('Fetching from Django at:', url);
      setLoading(true);

      try {
        const res = await fetch(url, {
          method: 'GET',
          credentials: 'include',
          headers: {
            'Accept': 'application/json'
          }
        });

        console.log('Status:', res.status, 'Content-Type:', res.headers.get('content-type'));
        if (!res.ok) throw new Error(`Status ${res.status}`);

        const data = await res.json();
        setItems(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }

    fetchItems();
  }, []);

  // Handler to add a new food item
  const handleAdd = async () => {
    if (!newItem.trim()) return;

    const url = `/api/${RESOURCE}/`;
    console.log('Posting to Django at:', url, 'with', newItem);

    try {
      const res = await fetch(url, {
        method: 'POST',
        credentials: 'include',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        body: JSON.stringify({ name: newItem })
      });

      console.log('Create status:', res.status);
      if (!res.ok) {
        const errData = await res.json();
        throw new Error(errData.detail || 'Create failed');
      }

      const created = await res.json();
      setItems(prev => [...prev, created]);
      setNewItem('');
    } catch (err) {
      setError(err.message);
    }
  };

  if (loading) return <div className="status">Loading…</div>;
  if (error)   return <div className="status error">Error: {error}</div>;

  return (
    <div className="App">
      <h1>NutriQuest</h1>

      <ul className="item-list">
        {items.map(item => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>

      <div className="controls">
        <input
          type="text"
          placeholder="New food item"
          value={newItem}
          onChange={e => setNewItem(e.target.value)}
        />
        <button onClick={handleAdd}>Add Item</button>
      </div>
    </div>
  );
}

export default App;