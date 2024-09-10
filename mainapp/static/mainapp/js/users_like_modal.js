const usersIsLiked = document.querySelectorAll('.customMouseMove');
    //   modalIsLikedUsers = document.querySelector('.')

usersIsLiked.forEach(element => {
    element.addEventListener('mousemove', () => {
        console.log('Mouse moved over the element');
    });
});