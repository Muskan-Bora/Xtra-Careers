/////////////////////////////////////////////////////

// Theme Toggle Logic
function toggleTheme() {
    const body = document.body;
    const toggleButton = document.getElementById('theme-toggle-btn');

    // Toggle between dark and light modes
    if (body.classList.contains('dark-mode')) {
        body.classList.replace('dark-mode', 'light-mode');
        toggleButton.textContent = '🌙'; // Update button icon
        localStorage.setItem('theme', 'light-mode');
    } else {
        body.classList.replace('light-mode', 'dark-mode');
        toggleButton.textContent = '☀️'; // Update button icon
        localStorage.setItem('theme', 'dark-mode');
    }
}

// Apply the saved theme on page load
window.onload = function () {
    const savedTheme = localStorage.getItem('theme') || 'light-mode';
    document.body.classList.add(savedTheme);

    // Update button icon based on the saved theme
    const toggleButton = document.getElementById('theme-toggle-btn');
    toggleButton.textContent = savedTheme === 'dark-mode' ? '☀️' : '🌙';
};

/////////////////////////////////////////////////////

// ----------- Toggle Button -------------------- //
function toggleMenu() {
    let buttons = document.querySelector('.nav-buttons');
    buttons.classList.toggle('active');
}

////////////////////////////////////////////////////////

// ---------------- Welcome Message ---------------------- //

const text = "Welcome to XtraCareers";  // Text to Type
const speed= 100; // Typing speed in milliseconds
let index= 0; // Current index of the text

function typeWriter() {
    if (index < text.length) {
        document.getElementById("type-writer").innerHTML += text.charAt(index);
        index++;
        setTimeout(typeWriter, speed); // call the function again after a delay
    }
}

// start typing once the DOM is fully loaded

document.addEventListener("DOMContentLoaded", function() {
    typeWriter();
});

//////////////////////////////////////////////////////////////////

// ------------------ Services -------------------------- //

document.addEventListener("DOMContentLoaded", function() {
    console.log("JavaScript is working!");

    let serviceSection = document.getElementById('services-section');
    if (serviceSection) {
        console.log("Service section found.");

        // Function to check if the service section is in the viewport
        function isElementInViewport(el) {
            const rect = el.getBoundingClientRect();
            return (
                rect.top >= 0 &&
                rect.left >= 0 &&
                rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
                rect.right <= (window.innerWidth || document.documentElement.clientWidth)
            );
        }

        // Function to reveal the service boxes with animation
        function revealServices() {
            const serviceBoxes = document.querySelectorAll('.service-box'); // Select all service boxes
            serviceBoxes.forEach((box, index) => {
                setTimeout(() => {
                    box.classList.add('show'); // Add the show class to animate
                }, index * 200); // Stagger the animation by 200ms
            });
        }

        // Check if the service section is in view when scrolling
        window.addEventListener('scroll', function() {
            if (isElementInViewport(serviceSection)) {
                console.log("Service section is in view.");
                revealServices(); // Trigger the reveal
                window.removeEventListener('scroll', arguments.callee); // Remove listener after triggering
            }
        });

        // Optional: Trigger on touchstart for mobile
        serviceSection.addEventListener('touchstart', function() {
            console.log("Service section touched.");
            revealServices(); // Trigger the reveal on touch
        });
    } else {
        console.log("Service section not found.");
    }
});

/////////////////////////////////////////////////////////////////////////

/* ----------------- About Us -------------------  */

document.addEventListener('DOMContentLoaded', function() {
    const aboutSection = document.querySelector('.aboutus-section');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                aboutSection.classList.add('show');
            }
        });
    }, {
        threshold: 0.5 // Trigger when 50% of the section is in view
    });

    observer.observe(aboutSection);
});

/////////////////////////////////////////////////////////////////////////////////////////////////

/* ---------------- FAQ's  --------------------- */ 

document.querySelectorAll('.faq-question').forEach(button => {
    button.addEventListener('click', () => {
        const answer = button.nextElementSibling;

        // Toggle active class for the question
        button.classList.toggle('active');

        // Slide up if already visible, else slide down
        if (answer.style.display === 'block') {
            answer.style.display = 'none';
        } else {
            document.querySelectorAll('.faq-answer').forEach(otherAnswer => {
                otherAnswer.style.display = 'none'; // Close all open answers
                otherAnswer.previousElementSibling.classList.remove('active'); // Remove active class from other questions
            });
            answer.style.display = 'block'; // Show the clicked answer
        }
    });
});

///////////////////////////////////////////////////////////////////////////////////

// Show button when reaching the blog section
document.addEventListener("DOMContentLoaded", function () {
    const scrollTopBtn = document.getElementById('scrollTopBtn');
    const faqSection = document.querySelector('#faq'); // Replace '#faq' with your FAQ section ID

    // Initially hide the button
    scrollTopBtn.style.display = "none";

    // Show or hide button based on scroll position
    window.onscroll = function () {
        if (faqSection && faqSection.getBoundingClientRect().top <= window.innerHeight) {
            scrollTopBtn.style.display = "block"; // Show the button
        } else {
            scrollTopBtn.style.display = "none"; // Hide the button
        }
    };
});

// Scroll to the top function
function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

///////////////////////////////////////////////////////////////////////////////////////////////////

function typeWriters(texts, elementId, speed) {
    let i = 0;

    function type() {
        const element = document.getElementById(elementId);
        if (element) {  // Check if the element exists
            if (i < texts.length) {
                element.innerHTML += texts.charAt(i);
                i++;
                setTimeout(type, speed);
            }
        }
    }

    type();
}

////////////////////////////////////////////////////////////////////////

document.addEventListener("DOMContentLoaded", function() {
    const serviceImageContainer = document.querySelector(".image-container1");
    const serviceTextContainer = document.querySelector(".text-container1");

    function animateServiceSection() {
        const windowHeight = window.innerHeight;
        const sectionTop = serviceImageContainer.getBoundingClientRect().top;

        if (sectionTop < windowHeight) {
            // Trigger animations by changing opacity and transform
            serviceImageContainer.style.opacity = 1;
            serviceImageContainer.style.transform = "translateX(0)"; // Slide to center

            serviceTextContainer.style.opacity = 1;
            serviceTextContainer.style.transform = "translateX(0)"; // Slide to center
        }
    }

    window.addEventListener("scroll", animateServiceSection);
    animateServiceSection(); // Initial check in case section is in view on load
});

document.addEventListener("DOMContentLoaded", function() {
    const serviceImageContainer1 = document.querySelector(".image-container2");
    const serviceTextContainer1 = document.querySelector(".text-container2");

    function animateServiceSection() {
        const windowHeight = window.innerHeight;
        const sectionTop = serviceImageContainer1.getBoundingClientRect().top;

        if (sectionTop < windowHeight) {
            // Trigger animations by changing opacity and transform
            serviceImageContainer1.style.opacity = 1;
            serviceImageContainer1.style.transform = "translateX(0)"; // Slide to center

            serviceTextContainer1.style.opacity = 1;
            serviceTextContainer1.style.transform = "translateX(0)"; // Slide to center
        }
    }

    window.addEventListener("scroll", animateServiceSection);
    animateServiceSection(); // Initial check in case section is in view on load
});

document.addEventListener("DOMContentLoaded", function() {
    const serviceImageContainer3 = document.querySelector(".image-container3");
    const serviceTextContainer3 = document.querySelector(".text-container3");

    function animateServiceSection() {
        const windowHeight = window.innerHeight;
        const sectionTop = serviceImageContainer3.getBoundingClientRect().top;

        if (sectionTop < windowHeight) {
            // Trigger animations by changing opacity and transform
            serviceImageContainer3.style.opacity = 1;
            serviceImageContainer3.style.transform = "translateX(0)"; // Slide to center

            serviceTextContainer3.style.opacity = 1;
            serviceTextContainer3.style.transform = "translateX(0)"; // Slide to center
        }
    }

    window.addEventListener("scroll", animateServiceSection);
    animateServiceSection(); // Initial check in case section is in view on load
});

/////////////////////////////////////////////////////////////////////////////////////////////

document.addEventListener("DOMContentLoaded", function() {
    const options = {
        threshold: 0.3 // Adjusts visibility threshold for triggering
    };

    const observer = new IntersectionObserver(function(entries, observer) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                console.log("Pricing section is in view");
                const columns = document.querySelectorAll(".columns");
                columns.forEach((column, index) => {
                    setTimeout(() => {
                        column.style.opacity = "1";
                        column.style.animation = "fadeIn 0.5s ease forwards";
                    }, index * 300); // Stagger animation with delay
                });
                observer.unobserve(entry.target); // Stop observing
            }
        });
    }, options);

    // Check if pricing section is present in DOM
    const target = document.querySelector("#pricing-section");
    if (target) {
        observer.observe(target);
        console.log("Observer set on pricing section");
    } else {
        console.log("Pricing section not found");
    }
});

/////////////////////////////////////////////////////////////////////////////////////////////////

document.addEventListener('DOMContentLoaded', () => {
    const experienceRadios = document.querySelectorAll('input[name="experience_level"]');
    const serviceCheckboxes = document.querySelectorAll('input[name="selected_services"]');
    const totalAmountElement = document.getElementById('totalAmount');
    const discountAmountElement = document.getElementById('discountAmount');
    const finalAmountElement = document.getElementById('finalAmount');
    const agreeTermsCheckbox = document.getElementById('agreeTerms');
    const payNowButton = document.getElementById('payNowButton');

    // Pricing structure for each service based on experience level (0-3)
    const pricing = {
        'ATS Optimized Resume and Cover Letter': [1500, 2000, 3000, 4000],
        // 'ATS Optimization': [250, 500, 750, 1000],
        'Personal Branding (LinkedIn)': [1000, 1500, 2000, 2500],
        'Mock Interviews and Guidance': [1500, 2500, 5000, 10000],
    };

    let selectedExperienceIndex = null; // Track selected experience level

    // Function to calculate the total amount
    function calculateTotal() {
        let total = 0;

        // Check if an experience level is selected
        if (selectedExperienceIndex !== null) {
            // Loop through each selected service and add the price to the total
            serviceCheckboxes.forEach(checkbox => {
                if (checkbox.checked) {
                    const service = checkbox.value; // Get the service name (e.g., 'Resume & Cover Letter')
                    const servicePrice = pricing[service][selectedExperienceIndex]; // Get the price for the selected experience level
                    total += servicePrice; // Add the service price to the total
                }
            });
        }

        // Display the actual total (without discount)
        totalAmountElement.textContent = `Actual Total Amount: ₹ ${total}`;

        console.log('Actual Total:', total); // Log the total amount to check the value

        // Apply discounts based on the number of selected services
        const selectedServicesCount = getSelectedServicesCount();
        let discountRate = 0;

        if (selectedServicesCount === 2) {
            discountRate = 0.1; // 10% discount for 2 services
        } else if (selectedServicesCount === 3) {
            discountRate = 0.2; // 20% discount for 3 services
        }

        // Calculate discount amount
        const discountAmount = total * discountRate;

        // Calculate the final amount to pay after discount
        const discountedAmount = total - discountAmount;

        // Calculate GST (18% of the discounted amount)
        const gstAmount = discountedAmount * 0.18;

        // Calculate the final amount to pay after discount and adding GST
        const finalAmount = discountedAmount + gstAmount;

        // Update the UI
        discountAmountElement.textContent = `Discount: ₹ ${discountAmount.toFixed(2)}`;
        document.getElementById('gstAmount').textContent = `GST (18%): ₹ ${gstAmount.toFixed(2)}`;
        finalAmountElement.textContent = `Final Amount to Pay: ₹ ${finalAmount.toFixed(2)}`;

        console.log('Discount Amount:', discountAmount); // Log the discount amount
        console.log('GST Amount:', gstAmount); // Log the GST amount
        console.log('Final Amount:', finalAmount); // Log the final amount

        // Ensure the amount is at least 1
        //const finalAmountInPaise = finalAmount * 100;  // Convert the amount to paise

        const finalAmountInPaise = Math.max(Math.round(finalAmount * 100), 100);

        if (finalAmountInPaise >= 100) {
            document.getElementById('amount').value = finalAmountInPaise; // Set the amount
        } else {
            document.getElementById('amount').value = 100; // Set a default amount of ₹1 (100 paise)
        }

         // Update the hidden field with the calculated amount in paise
        document.getElementById('amount').value = finalAmount;

    }

    // Function to count the number of selected services
    function getSelectedServicesCount() {
        let count = 0;
        serviceCheckboxes.forEach(checkbox => {
            if (checkbox.checked) {
                count++;
            }
        });
        return count;
    }

    // Event listener for experience level selection (radio buttons)
    experienceRadios.forEach((radio, index) => {
        radio.addEventListener('change', () => {
            selectedExperienceIndex = index; // Update the selected experience level index
            console.log('Experience Level Changed:', selectedExperienceIndex); // Log experience index
            calculateTotal(); // Recalculate total amount whenever experience level changes
            togglePayNowButton(); // Check if "Pay Now" should be enabled
        });
    });

    // Event listener for service selection (checkboxes)
    serviceCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', calculateTotal);
    });

    // Function to enable/disable the "Pay Now" button based on the checkbox for agreeing to terms
    function togglePayNowButton() {
        if (agreeTermsCheckbox.checked) {
            payNowButton.disabled = false;
        } else {
            payNowButton.disabled = true;
        }
    }

    // Event listener for the terms checkbox
    agreeTermsCheckbox.addEventListener('change', togglePayNowButton);

    // Initially calculate total if the user already has selections
    calculateTotal();
});

//////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////

document.getElementById("pay-with-razorpay").onclick = function (e) {
    console.log("Preparing Razorpay options...");
    // The amount is rendered correctly here by Django and passed to JavaScript
    console.log("Amount:", "{{ amount|floatformat:2 }}");  // This will be rendered as a number by Django
    console.log("Order ID:", "{{ order_id }}");
    
    var options = {
        "key": "{{ razorpay_api_key }}", // Use your Razorpay Key ID
        "amount": "{{ amount|floatformat:2 }}" * 100,  // Amount in paise (multiply by 100)
        "currency": "INR",
        "name": "Xtra Careers",
        "description": "Payment for Services",
        "image": "", // Optional: You can add your logo here
        "order_id": "{{ order_id }}", // The order ID you generated earlier
        "handler": function (response) {
            console.log("Payment successful:", response);
            var payment_id = response.razorpay_payment_id;
            var order_id = response.razorpay_order_id;
            var signature = response.razorpay_signature;
            
            // Send the payment details to your server for verification
            var form = document.createElement("form");
            form.method = "POST";
            form.action = "{% url 'razorpay_payment' %}";  // Your Razorpay success callback URL
            
            var payment_id_field = document.createElement("input");
            payment_id_field.type = "hidden";
            payment_id_field.name = "razorpay_payment_id";
            payment_id_field.value = payment_id;
            form.appendChild(payment_id_field);

            var order_id_field = document.createElement("input");
            order_id_field.type = "hidden";
            order_id_field.name = "razorpay_order_id";
            order_id_field.value = order_id;
            form.appendChild(order_id_field);

            var signature_field = document.createElement("input");
            signature_field.type = "hidden";
            signature_field.name = "razorpay_signature";
            signature_field.value = signature;
            form.appendChild(signature_field);
            
            document.body.appendChild(form);
            form.submit();
        },
        "prefill": {
            "name": "{{ payment.name }}",
            "email": "{{ payment.email }}",
            "contact": "{{ payment.contact }}",
        },
        "theme": {
            "color": "#F37254"
        }
    };
    
    var rzp1 = new Razorpay(options);
    rzp1.open();
    e.preventDefault();
};
/////////////////////////////////////////////////////////////////////////////////////////////////////
