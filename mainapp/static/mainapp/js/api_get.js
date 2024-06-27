
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