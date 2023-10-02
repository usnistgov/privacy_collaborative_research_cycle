var sortDirection = 'asc';

// Function to toggle the sort direction between ascending and descending
function toggleSortDirection() {
    // Toggling the sort direction
    sortDirection = sortDirection === 'asc' ? 'desc' : 'asc';
    
    // Updating the sort icon based on the current sort direction
    document.getElementById('sortIcon').className = sortDirection === 'asc' ? 'fas fa-sort-up' : 'fas fa-sort-down';
    
    // Updating the sort direction text
    document.getElementById('sortDirection').innerText = sortDirection.toUpperCase();
    
    // Sorting the table immediately after changing the sort direction
    sortTable();
}

// Function to sort the table
function sortTable() {
    var table, rows, switching, i, x, y, shouldSwitch;
    table = document.querySelector("table");
    switching = true;

    // Loop continues until no more rows need switching
    while (switching) {
        switching = false;
        rows = table.rows;

        // Loop through all rows of the table
        for (i = 1; i < (rows.length - 1); i++) {
            shouldSwitch = false;
            x = rows[i].getElementsByTagName("TD")[document.getElementById("sortDropdown").value];
            y = rows[i + 1].getElementsByTagName("TD")[document.getElementById("sortDropdown").value];

            // If columns contain numbers, scientific notation, or a list of numbers
            if (document.getElementById("sortDropdown").value > 2) {
                var xVal, yVal;

                if (document.getElementById("sortDropdown").value == 6) { // If ε column
                    // Counting the number of elements in the list
                    xVal = x.innerHTML.length ? x.innerHTML.split(',').length : 0;
                    yVal = y.innerHTML.length ? y.innerHTML.split(',').length : 0;
        
                } else {
                    // For other numeric columns
                    xVal = parseFloat(x.innerHTML);
                    yVal = parseFloat(y.innerHTML);
                }

                // Compare numeric values
                if (sortDirection == "asc") {
                    if (xVal > yVal) {
                        shouldSwitch = true;
                        break;
                    }
                } else if (sortDirection == "desc") {
                    if (xVal < yVal) {
                        shouldSwitch = true;
                        break;
                    }
                }
            } else {
                // Compare string values
                if (sortDirection == "asc") {
                    if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                        shouldSwitch = true;
                        break;
                    }
                } else if (sortDirection == "desc") {
                    if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
                        shouldSwitch = true;
                        break;
                    }
                }
            }
        }

        // Switch the rows if needed
        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
        }
    }
}
