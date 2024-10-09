const msgShow = document.querySelector('.wrapper--alert-alert'),
      msgPositive = document.querySelector('.wrapper--alert-alert');

  if (msgShow) {
    msgShow.style.top = 100 + 'px'
    msgShow.style.opacity = 1;

    if (msgPositive || msgPositive) {
      setTimeout(() => {
        msgPositive.style.display = 'none';
      }, 6000);
    }
  }