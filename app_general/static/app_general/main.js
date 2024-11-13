const subscriptionForm = document.querySelector('.subscription-form');

function foodSetvalidation(event) {
    const checkedFoodSet = document.querySelectorAll('input[name="food_set"]:checked');
    if (checkedFoodSet.length === 0) {
        event.preventDefault();
        alert('Please select a menu');
    }
}

if (!!subscriptionForm) {
    subscriptionForm.addEventListener('submit', foodSetvalidation);
}