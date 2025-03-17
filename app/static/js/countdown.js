document.addEventListener('DOMContentLoaded', () => {
	// Function to calculate time remaining to next birthday
	function calculateTimeRemaining(birthdayDate) {
		const today = new Date();
		const birthday = new Date(birthdayDate);

		// Set birthday to this year
		birthday.setFullYear(today.getFullYear());

		// If this year's birthday has passed, set to next year
		if (birthday < today) {
			birthday.setFullYear(today.getFullYear() + 1);
		}

		// Calculate time difference
		const timeDiff = birthday.getTime() - today.getTime();

		// Calculate days, hours, minutes, seconds
		const days = Math.floor(timeDiff / (1000 * 60 * 60 * 24));
		const hours = Math.floor((timeDiff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
		const minutes = Math.floor((timeDiff % (1000 * 60 * 60)) / (1000 * 60));
		const seconds = Math.floor((timeDiff % (1000 * 60)) / 1000);

		return { days, hours, minutes, seconds };
	}

	// Update countdown timers
	function updateCountdowns() {
		const countdownElements = document.querySelectorAll('.countdown-timer');

		countdownElements.forEach(el => {
			const birthdayDate = el.getAttribute('data-birthday');
			const { days, hours, minutes, seconds } = calculateTimeRemaining(birthdayDate);

			el.textContent = `Next birthday in: ${days} days, ${hours} hours, ${minutes} minutes, ${seconds} seconds`;
		});
	}

	// Initial update
	updateCountdowns();

	// Update every second
	setInterval(updateCountdowns, 1000);
});
