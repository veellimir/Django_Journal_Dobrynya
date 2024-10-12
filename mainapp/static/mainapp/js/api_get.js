
export function fetchEvents() {
    return fetch("/api/events/")
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then((data) => {
        let events = data;
        return events;
      })
      .catch((error) => {
        return;
    });
}

export function getCancelEvent() {
  return fetch('/api/cancel-event/')
      .then(response => response.json())
      .then(data => {
        return Array.isArray(data) ? data : [];
      })
      .catch(error => {
        console.error('error list cancel event:', error);
        return [];
      });
}


export function fetchAttendance(month, year) {
  return fetch(`/api/attendance/?month=${month}&year=${year}`)
    .then((response) => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then((data) => {
      return data;
      
    })
    .catch((error) => {
      console.error('Fetch error:', error);
      return [];
    });
}