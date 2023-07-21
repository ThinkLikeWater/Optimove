### 1.Test Case: Valid Country Name

- Input: "Ukraine"
- Expected Output: Verify that the response contains information about Ukraine, such as country name, capital, population, etc.

### 2.Test Case: Another Valid Country Name

- Input: "Germany"
- Expected Output: Verify that the response contains information about Germany, such as country name, capital, population, etc.

### 3. Test Case: Country Name with Special Characters

- Input: "Côte d'Ivoire"
- Expected Output: Verify that the response contains information about Côte d'Ivoire, handling special characters correctly.

### 4. Test Case: Non-Existent Country Name

- Input: "NonExistentCountry"
- Expected Output: Verify that the response returns an appropriate error message or status code (e.g., 404 Not Found) indicating that the country doesn't exist.

### 5. Test Case: Boundary Test with Short Country Name

- Input: A very short country name (e.g., "A").
- Expected Output: Verify that the endpoint correctly handles and responds to the minimum allowed length for a country name.

### 6. Test Case: Localization Test

- Input: Country name in a different language (e.g., "République française" for France).
- Expected Output: Verify that the endpoint correctly handles and responds to country names in different languages.
