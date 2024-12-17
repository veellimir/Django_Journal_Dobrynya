
// export function fetchEvents(all) {
//     return fetch("/api/events/")
//       .then((response) => {
//         if (!response.ok) {
//           throw new Error('Network response was not ok');
//         }
//         return response.json();
//       })
//       .then((data) => {
//         let events = data;
//         return events;
//       })
//       .catch((error) => {
//         return;
//     });
// }
export function fetchEvents(all) {
  const url = new URL("/api/events/", window.location.origin); // базовый URL API
  const params = new URLSearchParams();

  // Если параметр 'all' равен true, добавляем его в параметры запроса
  if (all) {
      params.append("all", "true");
  } else {
      params.append("all", "false");
  }

  // Добавляем параметры к URL
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