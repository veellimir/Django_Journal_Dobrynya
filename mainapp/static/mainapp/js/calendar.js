import { fetchEvents } from './api_get.js';

let today = new Date(),
    currentMonth = today.getMonth(),
    currentYear = today.getFullYear();

const months = [
    "Январь",
    "Февраль",
    "Март",
    "Апрель",
    "Май",
    "Июнь",
    "Июль",
    "Август",
    "Сентябрь",
    "Октябрь",
    "Ноябрь",
    "Декабрь",
  ],
  weekdays = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"];

function displayEvents(date) {
    let eventDate = date.toDateString();
    document.getElementById("event-date").textContent = eventDate;

  fetchEvents()
    .then((events) => {
      generateCalendar(currentMonth, currentYear, events);
    })
    .catch((error) => {
      generateCalendar(currentMonth, currentYear, []);
  });
}

function generateCalendar(month, year, events) {
  let firstDay = new Date(year, month, 1),
      lastDay = new Date(year, month + 1, 0),
      numDays = lastDay.getDate(),
      startingDay = (firstDay.getDay() + 6) % 7;

  document.getElementById("month-year").textContent =
    months[month] + " " + year;

  let calendarDates = document.getElementById("calendar-dates");
  calendarDates.innerHTML = "";

  let weekdaysRow = document.getElementById("weekdays");
  weekdaysRow.innerHTML = "";

  for (let weekday of weekdays) {
    let th = document.createElement("th");
    th.textContent = weekday;
    weekdaysRow.appendChild(th);
  }

  let date = 1,
      currentWeekday = startingDay;

  for (let i = 0; i < 6; i++) {
    let row = document.createElement("tr");

    for (let j = 0; j < 7; j++) {
      let cell = document.createElement("td");

      if (i === 0 && j < startingDay) {
        cell.textContent = "";

      } else if (date > numDays) {
        cell.textContent = "";

      } else {
        let eventDiv = document.createElement("div");
        eventDiv.textContent = date;
        cell.appendChild(eventDiv);

        let currentDayOfWeek = weekdays[currentWeekday];
        cell.setAttribute("data-weekday", currentDayOfWeek);

        if (events && events.length > 0) {
          events.forEach((event) => {
            if (event.days_of_week.includes(currentDayOfWeek.toLowerCase())) {
              let eventNameDiv = document.createElement("div");

              eventNameDiv.textContent = event.name;
              eventNameDiv.classList.add("event-name");
              cell.appendChild(eventNameDiv);

              eventNameDiv.addEventListener('click', () => {
                openModal(event);
              });
            }
          });
        }
        date++;
        currentWeekday = (currentWeekday + 1) % 7;
      }
      row.appendChild(cell);
    }
    calendarDates.appendChild(row);
  }
}

function openModal(event) {
  const modal = document.getElementById("modal"),
        modalTitle = document.getElementById("modal-title"),
        modalName = document.getElementById("modal-name"),
        modalStartTime = document.getElementById("modal-start_time"),
        modalEndTime = document.getElementById("modal-end_time");

  modalName.textContent = event.name;
  modalTitle.textContent = `Описания: ${event.title}`;
  modalStartTime.textContent = `Время начало : ${event.start_time}`;
  modalEndTime.textContent = `Конец в : ${event.end_time}`;

  modal.style.display = "block";
}

function closeModal() {
  const modal = document.getElementById("modal");
  modal.style.display = "none";
}

const span = document.getElementsByClassName("close")[0];
span.addEventListener('click', closeModal);

window.addEventListener('click', (event) => {
  const modal = document.getElementById("modal");
  if (event.target == modal) {
    modal.style.display = "none";
  }
});

const previousMonth = document.querySelector('.previousMonth'),
      nextMonth = document.querySelector('.nextMonth');

previousMonth.addEventListener('click', () => {
  currentMonth--;

  if (currentMonth < 0) {
    currentMonth = 11;
    currentYear--;
  }
  displayEvents(new Date(currentYear, currentMonth));
})

nextMonth.addEventListener('click', () => {
  currentMonth++;

  if (currentMonth > 11) {
    currentMonth = 0;
    currentYear++;
  }
  displayEvents(new Date(currentYear, currentMonth));
})

displayEvents(new Date(currentYear, currentMonth));












