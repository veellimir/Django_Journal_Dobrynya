export function fetchEvents(filterType = 'mine') {
  const url = new URL("/api/events/", window.location.origin),
        params = new URLSearchParams();

  params.append("filter", filterType);
  url.search = params.toString();

  return fetch(url)
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
      console.error('Error fetching events:', error);
      return [];
  });
}

export function getCancelEvent() {
  return fetch('/api/cancel-event/')
      .then(response => response.json())
      .then(data => {
        return Array.isArray(data) ? data : [];
      })
      .catch(error => {
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
      return [];
    });
}