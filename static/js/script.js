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
