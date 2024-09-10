import { fetchEvents, fetchAttendance } from './api_get.js';

let today = new Date(),
    currentMonth = today.getMonth() +1,
    currentYear = today.getFullYear();

const months = [
    "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль",
    "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
];
const weekdays = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"];

let attendanceData = [];

function displayEvents(date) {
    let eventDate = date.toDateString();
    document.getElementById("event-date").textContent = eventDate;

    Promise.all([fetchEvents(), fetchAttendance(currentMonth, currentYear)])
        .then(([events, attendance]) => {
            attendanceData = attendance;
            generateCalendar(currentMonth-1, currentYear, events);
        })
        .catch((error) => {
            console.error('Error fetching data:', error);
            generateCalendar(currentMonth-1, currentYear, []);
        });
}

function generateCalendar(month, year, events) {
    let firstDay = new Date(year, month, 1),
        lastDay = new Date(year, month + 1, 0),
        numDays = lastDay.getDate(),
        startingDay = (firstDay.getDay() + 6) % 7;

    document.getElementById("month-year").textContent = `${months[month]} ${year}`;

    let calendarDates = document.getElementById("calendar-dates");
    calendarDates.innerHTML = "";

    let weekdaysRow = document.getElementById("weekdays");
    weekdaysRow.innerHTML = weekdays.map(day => `<th>${day}</th>`).join('');

    let date = 1,
        currentWeekday = startingDay;

    for (let i = 0; i < 6; i++) {
        let row = document.createElement("tr");

        for (let j = 0; j < 7; j++) {
            let cell = document.createElement("td");

            if (i === 0 && j < startingDay || date > numDays) {
                cell.textContent = "";
            } else {
                let eventDiv = document.createElement("div");
                eventDiv.textContent = date;
                cell.appendChild(eventDiv);

                let currentDayOfWeek = weekdays[currentWeekday];
                cell.setAttribute("data-weekday", currentDayOfWeek);

                cell.addEventListener('click', () => {
                    handleDateClick(cell);
                });


                updateEvents(cell, date, currentDayOfWeek, events);
                date++;

                currentWeekday = (currentWeekday + 1) % 7;
            }
            row.appendChild(cell);
            
        }
        calendarDates.appendChild(row);
    }
}

function updateEvents(cell, date, currentDayOfWeek, events) {
    if (events && events.length > 0) {
        events.forEach((event) => {
            if (event.days_of_week.includes(currentDayOfWeek.toLowerCase())) {
                let eventNameDiv = document.createElement("div"),
                    displayText = event.training_direction_name;

                eventNameDiv.textContent = displayText;
                eventNameDiv.classList.add("event-name");
                eventNameDiv.style.backgroundColor = event.elem_color;

                cell.appendChild(eventNameDiv);
                eventNameDiv.addEventListener('click', () => {
                    openModal(event, date);
                });
            }
        });
    }
}

function handleDateClick(cell) {
    const dayDiv = cell.querySelector('div');
    const dayNumber = dayDiv ? parseInt(dayDiv.textContent, 10) : null;

    if (dayNumber === null) {
        return null;
    }

    return {
        date: new Date(currentYear, currentMonth - 1, dayNumber),
        dayNumber: dayNumber
    };
}

function openModal(event, date) {
    const coachDetails = event.teacher.map(coach => `${coach.surname} ${coach.name} ${coach.patronymic}`).join(", "),
          modal = document.getElementById("modal"),
          modalTeacher = document.getElementById("modal-teacher"),
          modalTitle = document.getElementById("modal-title"),
          modalName = document.getElementById("modal-name"),
          modalStartTime = document.getElementById("modal-start_time"),
          modalEndTime = document.getElementById("modal-end_time"),
          modalProfileUser = document.getElementById("modal-profile_user");

    if (event.teacher.length === 0) {
        modalTeacher.textContent = 'Преподаватель: преподаватель ещё не назначен';
    } else if (event.teacher.length === 1) {
        modalTeacher.textContent = `Преподаватель: ${coachDetails}`;
    } else {
        const lastIndex = coachDetails.lastIndexOf(", "),
              coaches = coachDetails.substring(0, lastIndex),
              lastCoach = coachDetails.substring(lastIndex + 2);
        
        modalTeacher.textContent = `Преподаватели: ${coaches}, ${lastCoach}`;
    }

    modalName.textContent = event.training_direction_name;
    modalTitle.textContent = `Описания: ${event.title}`;
    modalStartTime.textContent = `Время начало: ${event.start_time}`;
    modalEndTime.textContent = `Конец в: ${event.end_time}`;

    const formatDate = (date) => {
        if (!date) return null;
            const d = new Date(date),
                year = d.getFullYear(),
                month = String(d.getMonth() + 1).padStart(2, '0'),
                day = String(d.getDate()).padStart(2, '0');
            return `${year}-${month}-${day}`;
    };

    const matchingAttendees = attendanceData.filter(att => {
        const attendanceDateString = formatDate(att.date),
              formattedMonth = String(currentMonth).padStart(2, '0'),
              formattedDate = String(date).padStart(2, '0'),
              selectCurrentDate = `${currentYear}-${formattedMonth}-${formattedDate}`;

        return attendanceDateString === selectCurrentDate && att.training_direction_name === event.training_direction_name;
    });

    const participantInfo = matchingAttendees.length > 0
    ? matchingAttendees.map(att => `${att.profile_surname} ${att.is_present ? '✅' : '❌'}`).join("<br> ")
    : "Нет данных о посещении";

    modalProfileUser.innerHTML = `Посещаемость участников: <hr> ${participantInfo}`;
    modal.style.display = "block";
}

function closeModal() {
    const modal = document.getElementById("modal"),
          btnCancelWorkout = document.getElementById("cancelWorkout"),
          containerCancelWorkout = document.getElementById("containerCancelWorkout");

    if (containerCancelWorkout) {
        containerCancelWorkout.classList.remove('show');
        btnCancelWorkout.style.display = '';
    }
    modal.style.display = 'none';
}

const span = document.getElementsByClassName("close")[0];
span.addEventListener('click', closeModal);

window.addEventListener('click', (event) => {
    const modal = document.getElementById("modal");
    if (event.target === modal) {
        closeModal();
    }
});

const previousMonth = document.querySelector(".previousMonth"),
      nextMonth = document.querySelector(".nextMonth");

previousMonth.addEventListener('click', () => {
    currentMonth--;
    if (currentMonth < 1) {
        currentMonth = 12;
        currentYear--;
    }
    displayEvents(new Date(currentYear, currentMonth));
})

nextMonth.addEventListener('click', () => {
    currentMonth++;
    if (currentMonth > 12) {
        currentMonth = 1;
        currentYear++;
    }
    displayEvents(new Date(currentYear, currentMonth -1));
})

displayEvents(new Date(currentYear, currentMonth -1));

const btnCancelWorkout = document.getElementById('cancelWorkout'),
      containerCancelWorkout = document.getElementById('containerCancelWorkout');

btnCancelWorkout.addEventListener('click', () => {
    containerCancelWorkout.classList.add('show');
    btnCancelWorkout.style.display = 'none';
});
