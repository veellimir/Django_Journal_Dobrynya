
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