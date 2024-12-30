// search bar 
document.addEventListener('DOMContentLoaded', function () {
    const searchTrigger = document.getElementById('searchButton');
    const searchInput = document.getElementById('searchInput');
    const closeSearch = document.getElementById('closeSearch');

    // Trigger search input expansion
    searchTrigger.addEventListener('click', function (e) {
        if (!searchInput.classList.contains('show')) {
            e.preventDefault(); // Prevent form submission on expand
            searchInput.classList.add('show');
            closeSearch.classList.add('show');
        }
    });

    // Close search input
    closeSearch.addEventListener('click', function () {
        searchInput.classList.remove('show');
        closeSearch.classList.remove('show');
    });

    searchInput.addEventListener('keydown', function (e) {
        if (e.key === 'Enter') {
            document.querySelector('.search-bar').submit();
        }
    });
});


// Show/Hide Back to Top Button on Scroll (shop app styling)
const backToTopBtn = document.getElementById('bttBtn');

window.addEventListener('scroll', () => {
    if (window.scrollY > 300) {
        backToTopBtn.classList.remove('hidden');
        backToTopBtn.classList.add('visible');
    } else {
        backToTopBtn.classList.remove('visible');
        backToTopBtn.classList.add('hidden');
    }
});

// Scroll to top when clicked
backToTopBtn.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth',
    });
});


