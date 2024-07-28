    
    document.addEventListener("DOMContentLoaded", function() {
        const phoneInput = document.querySelector('input[name="phone"]');

        new Cleave(phoneInput, {
            phone: true,
            phoneRegionCode: 'RU',
            delimiter: ' ',
            blocks: [0, 3, 3, 2, 2],
            prefix: '+7 '
        });
    });