import { fetchEvents, fetchAttendance, getCancelEvent } from "./api_get.js";

let today = new Date(),
    currentMonth = today.getMonth() + 1,
    currentYear = today.getFullYear(),
    attendanceData = [];

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
weekdays = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"],
spinner = document.querySelector('.spinner');

document.addEventListener("DOMContentLoaded", function () {
  const filterMineButton = document.getElementById('filter-mine'),
        filterAllButton = document.getElementById('filter-all'),
        filterEventsButton = document.getElementById('filter-events');

  let filter_type = 'mine';

  if (filterMineButton) {
    filterMineButton.addEventListener('click', function () {
      filter_type = 'mine';
      displayEvents(filter_type);
    });
  }

  if (filterAllButton) {
    filterAllButton.addEventListener('click', function () {
      filter_type = 'all';
      displayEvents(filter_type);
    });
  }

  if (filterEventsButton) {
    filterEventsButton.addEventListener('click', function () {
      filter_type = "competition";
      displayEvents(filter_type);
    });
  }


function displayEvents(filterType) {
    if (filterType === "competition") {
      displayedCompetitionDates = [];
    }
  
    Promise.all([fetchEvents(filterType), fetchAttendance(currentMonth, currentYear), getCancelEvent()])
      .then(([events, attendance, cancelEvents]) => {
        attendanceData = attendance;
        generateCalendar(currentMonth - 1, currentYear, events, cancelEvents, filterType);
        if (spinner) {
          spinner.style.display = 'none';
        }
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
        generateCalendar(currentMonth - 1, currentYear, [], [], filterType);
      });
  }
  
  
function generateCalendar(month, year, events, cancelEvents, filterType) {
    let firstDay = new Date(year, month, 1),
        lastDay = new Date(year, month + 1, 0),
        numDays = lastDay.getDate(),
        startingDay = (firstDay.getDay() + 6) % 7;
  
    document.getElementById("month-year").textContent = `${months[month]} ${year}`;
  
    let calendarDates = document.getElementById("calendar-dates");
    if (calendarDates) {
      calendarDates.innerHTML = "";
    }
  
    let weekdaysRow = document.getElementById("weekdays");
    if (weekdaysRow) {
      weekdaysRow.innerHTML = weekdays.map((day) => `<th>${day}</th>`).join("");
    }
  
    let date = 1,
        currentWeekday = startingDay;
  
    for (let i = 0; i < 6; i++) {
      let row = document.createElement("tr");
  
      for (let j = 0; j < 7; j++) {
        let cell = document.createElement("td");
  
        if ((i === 0 && j < startingDay) || date > numDays) {
          cell.textContent = "";
        } else {
          let eventDiv = document.createElement("div");
          eventDiv.textContent = date;
          cell.appendChild(eventDiv);
  
          let currentDayOfWeek = weekdays[currentWeekday];
          cell.setAttribute("data-weekday", currentDayOfWeek);
  
          const cellDate = new Date(year, month, date);
  
          if (cellDate.toDateString() === today.toDateString()) {
            cell.style.backgroundColor = "#7DA58D";
          } else if (cellDate < today) {
            cell.style.backgroundColor = "#d3d3d3";
          }
  
          cell.addEventListener("click", () => {
            handleDateClick(cell);
          });
  
          updateEvents(cell, date, currentDayOfWeek, events, cancelEvents, filterType);
          date++;
          currentWeekday = (currentWeekday + 1) % 7;
        }
        row.appendChild(cell);
      }
      calendarDates.appendChild(row);
    }
  }
  

let displayedCompetitionDates = [];

function updateEvents(cell, date, currentDayOfWeek, events, cancelEvents, filterType) {
  const cellDate = new Date(currentYear, currentMonth - 1, date);

  if (events && events.length > 0) {
    const filteredEvents = events.filter(event => {
      if (filterType === "competition") {
        const eventDate = new Date(event.event_date);
        return eventDate.toDateString() === cellDate.toDateString();
      }
      return event.days_of_week.includes(currentDayOfWeek.toLowerCase());
    });

    filteredEvents.sort((a, b) => {
      const timeA = new Date(`1970-01-01T${a.start_time}`);
      const timeB = new Date(`1970-01-01T${b.start_time}`);
      return timeA - timeB;
    });

    filteredEvents.forEach(event => {
      let eventNameDiv = document.createElement("div"),
          displayText = `${event.training_direction_name} <br> ${event.start_time} - ${event.end_time}`;

      eventNameDiv.innerHTML = displayText;
      eventNameDiv.classList.add("event-name");
      eventNameDiv.style.backgroundColor = event.elem_color;

      const now = new Date(),
            eventStartTime = new Date(`${cellDate.toDateString()} ${event.start_time}`),
            eventEndTime = new Date(`${cellDate.toDateString()} ${event.end_time}`);

      if (eventEndTime < now) {
        eventNameDiv.style.backgroundColor = "#CCFFCC";
      }

      const isCanceled = cancelEvents.find(cancelEvent => {
        const cancelDate = new Date(cancelEvent.cancelled_date);
        return (
          cancelDate.getFullYear() === cellDate.getFullYear() &&
          cancelDate.getMonth() === cellDate.getMonth() &&
          cancelDate.getDate() === cellDate.getDate() &&
          event.training_direction_name === cancelEvent.cancelled_title
        );
      });

      if (isCanceled) {
        eventNameDiv.style.backgroundColor = "#e25050";
        eventNameDiv.innerHTML = `${event.training_direction_name} <br> <b>Тренировка отменена</b> ☢️`;
      }

      cell.appendChild(eventNameDiv);
      eventNameDiv.addEventListener("click", () => {
        openModal(event, date, isCanceled);
      });
    });
  }
}


function handleDateClick(cell) {
    const dayDiv = cell.querySelector("div"),
          dayNumber = dayDiv ? parseInt(dayDiv.textContent, 10) : null;

    if (dayNumber === null) {
      return null;
    }
    return {
      date: new Date(currentYear, currentMonth - 1, dayNumber),
      dayNumber: dayNumber,
    };
}


function openModal(event, date, isCanceled) {
    const coachDetails = event.teacher.map((coach) => `${coach.surname} ${coach.name} ${coach.patronymic}`).join(", "),
          modal = document.getElementById("modal"),
          modalTeacher = document.getElementById("modal-teacher"),
          modalTitle = document.getElementById("modal-title"),
          modalName = document.getElementById("modal-name"),
          modalStartTime = document.getElementById("modal-start_time"),
          modalEndTime = document.getElementById("modal-end_time"),
          modalProfileUser = document.getElementById("modal-profile_user"),
          blockCancelLesson = document.querySelector('.customCancelLesson');

    if (event.teacher.length === 0) {
      modalTeacher.textContent = "Преподаватель: преподаватель ещё не назначен";
    } else if (event.teacher.length === 1) {
      modalTeacher.textContent = `Преподаватель: ${coachDetails}`;
    } else {
      const lastIndex = coachDetails.lastIndexOf(", "),
            coaches = coachDetails.substring(0, lastIndex),
            lastCoach = coachDetails.substring(lastIndex + 2);

      modalTeacher.textContent = `Преподаватели: ${coaches}, ${lastCoach}`;
    }
    modalName.textContent = event.training_direction_name;
    
    if (isCanceled) {
        modalStartTime.innerHTML = `<b class='text-danger'>Тренировка отменена<b> <br>Причина: ${isCanceled.description}`;
        modalTitle.textContent = "";
        modalEndTime.textContent = "";
    } else {
        modalTitle.textContent = `Описания: ${event.title}`;
        modalStartTime.textContent = `Время начало: ${event.start_time}`;
        modalEndTime.textContent = `Конец в: ${event.end_time}`;
    }

    const today = new Date(),
          eventDate = new Date(currentYear, currentMonth - 1, date);

    blockCancelLesson.style.display = eventDate < today ? "none" : "";

    const formatDate = (date) => {
        if (!date) return null;
        const d = new Date(date),
              year = d.getFullYear(),
              month = String(d.getMonth() + 1).padStart(2, "0"),
              day = String(d.getDate()).padStart(2, "0");
        return `${year}-${month}-${day}`;
    };

    const matchingAttendees = attendanceData.filter((att) => {
        const attendanceDateString = formatDate(att.date),
              formattedMonth = String(currentMonth).padStart(2, "0"),
              formattedDate = String(date).padStart(2, "0"),
              selectCurrentDate = `${currentYear}-${formattedMonth}-${formattedDate}`;

        return (
            attendanceDateString === selectCurrentDate &&
            att.training_direction_name === event.training_direction_name
        );
    });

    const participantInfo =
        matchingAttendees.length > 0
            ? matchingAttendees
                .map((att) => `${att.profile_surname} ${att.is_present ? "✅" : "❌"}`)
                .join("<br> ")
            : "Нет данных о посещении";

    modalProfileUser.innerHTML = `Посещаемость участников: <hr> ${participantInfo}`;
    modal.style.display = "block";
}


function closeModal() {
    const modal = document.getElementById("modal");
    modal.style.display = "none";
}


const span = document.getElementsByClassName("close")[0];
  if (span) {
    span.addEventListener("click", closeModal);
  }

  window.addEventListener("click", (event) => {
    const modal = document.getElementById("modal");
    if (modal && event.target === modal) {
      closeModal();
    }
  });


const previousMonth = document.querySelector(".previousMonth"),
        nextMonth = document.querySelector(".nextMonth"),
        currentMY = document.getElementById("month-year");

  if (previousMonth && nextMonth) {
    if (currentMY.textContent === "Октябрь 2024") {
      previousMonth.style.display = "none";
      previousMonth.disabled = true;
    }

    previousMonth.addEventListener("click", () => {
      if (currentMY.textContent !== "Октябрь 2024") {
        currentMonth--;
        if (currentMonth < 1) {
          currentMonth = 12;
          currentYear--;
        }
        displayEvents();
      }
    });

    nextMonth.addEventListener("click", () => {
      currentMonth++;
      if (currentMonth > 12) {
        currentMonth = 1;
        currentYear++;
      }
      displayEvents();
    });
}
displayEvents();


const btnCancelWorkout = document.getElementById("cancelWorkout");
  if (btnCancelWorkout) {
    btnCancelWorkout.addEventListener("click", () => {
        btnCancelWorkout.style.display = "none";
    });
  }
});

