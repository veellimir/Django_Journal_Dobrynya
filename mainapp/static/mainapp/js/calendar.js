let today = new Date(),
    currentMonth = today.getMonth(),
    currentYear = today.getFullYear(),
    selectedDate = new Date(today);

const months = ['Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь'],
      weekdays = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье'];

function generateCalendar(month, year) {
  let firstDay = new Date(year, month, 1),
      lastDay = new Date(year, month + 1, 0),
      numDays = lastDay.getDate(),
      startingDay = firstDay.getDay();

  document.getElementById('month-year').textContent = months[month] + ' ' + year;

  let calendarDates = document.getElementById('calendar-dates');
  calendarDates.innerHTML = '';

  let weekdaysRow = document.getElementById('weekdays');
  weekdaysRow.innerHTML = '';

  for (let weekday of weekdays) {
    let th = document.createElement('th');
    th.textContent = weekday;
    weekdaysRow.appendChild(th);
  }

  let date = 2;
  for (let i = 0; i < 6; i++) {
    let row = document.createElement('tr');

    for (let j = 0; j < 7; j++) {
      if (i === 0 && j < startingDay) {
        let cell = document.createElement('td');
        row.appendChild(cell);

      } else if (date > numDays) {
        break;

      } else {
        let cell = document.createElement('td');
        cell.textContent = date;

        if (date === today.getDate() && year === today.getFullYear() && month === today.getMonth()) {
          cell.classList.add('today');
        }

        cell.addEventListener('click', function() {
          selectDate(new Date(year, month, date));
        });
        row.appendChild(cell);
        date++;
      }
    }
    calendarDates.appendChild(row);
  }

  displayEvents(selectedDate);
}

function displayEvents(date) {
  let eventDate = date.toDateString();
  document.getElementById('event-date').textContent = eventDate;

  let eventsList = document.getElementById('events-list');
  eventsList.innerHTML = '';
  let events = [
    { time: '10:00 AM', title: 'Meeting' },
    { time: '2:00 PM', title: 'Lunch with friends' },
    { time: '6:00 PM', title: 'Birthday party' }
  ];

  events.forEach(event => {
    let li = document.createElement('li');
    li.textContent = `${event.time} - ${event.title}`;
    eventsList.appendChild(li);
  });
}

function selectDate(date) {
  selectedDate = date;
  generateCalendar(selectedDate.getMonth(), selectedDate.getFullYear());
}

function previousMonth() {
  currentMonth--;

  if (currentMonth < 0) {
        currentMonth = 11;
        currentYear--;
  }
  generateCalendar(currentMonth, currentYear);
}

function nextMonth() {
  currentMonth++;

  if (currentMonth > 11) {
        currentMonth = 0;
        currentYear++;
  }
  generateCalendar(currentMonth, currentYear);
}

generateCalendar(currentMonth, currentYear);
