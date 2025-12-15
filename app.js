Array.from(document.getElementsByTagName('input')).forEach((e , i)=>{
    e.addEventListener('keyup', (el)=>{
        if (e.value.length > 0) {
            document.getElementsByClassName('bi-caret-down-fill')[i].style.transform = "rotate(180deg)";
        } else {
            document.getElementsByClassName('bi-caret-down-fill')[i].style.transform = "rotate(0deg)";
        }
    })
})

let menu_btn = document.getElementsByClassName('bi-three-dots')[0];
let menu_bx = document.getElementById('menu_bx');


menu_btn.addEventListener('click', ()=>{
    menu_bx.classList.toggle('ul_active');
})

// Function to handle successful registration

function onRegistrationSuccess() {

    // Redirect to the new page

    window.location.href = 'after.html';

}

// Add event listener for the Venue option
const venueOption = document.getElementById('venue-option');
const stateDropdown = document.getElementById('state-dropdown');

venueOption.addEventListener('click', (event) => {
    event.preventDefault(); // Prevent default link behavior
    // Toggle dropdown visibility
    const isVisible = stateDropdown.style.display === 'block';
    stateDropdown.style.display = isVisible ? 'none' : 'block';

    // Populate the dropdown with states if not already populated
    if (!isVisible && stateDropdown.children.length === 0) {
        const states = [
           "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Delhi",
        "Goa", "Gujarat", "Haryana", "Himachal Pradesh",
        "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
         "Punjab",
        "Rajasthan", "Sikkim", 
        "Uttar Pradesh", "Uttarakhand", "West Bengal"
        ];

        states.forEach(state => {
            const li = document.createElement('li');
            li.textContent = state;
            li.addEventListener('click', () => {
                alert(`You selected: ${state}`); // Handle state selection
                stateDropdown.style.display = 'none'; // Hide dropdown after selection
            });
            stateDropdown.appendChild(li);
        });
    }
});

// Example usage: Call this function after successful registration

// onRegistrationSuccess();

