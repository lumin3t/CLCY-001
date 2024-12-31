const { scryptSync, randomBytes, timingSafeEqual } = require("crypto");

function hashPassword(password, salt = randomBytes(16).toString("hex")) {
  // Use scryptSync to hash the password with the salt
  const hashedPassword = scryptSync(password, salt, 64).toString("hex");
  return { hashedPassword, salt };
}

function verifyPassword(inputPassword, storedHash, salt) {
  // Hash the input password with the stored salt
  const inputHash = scryptSync(inputPassword, salt, 64).toString("hex");
  // Use timingSafeEqual to compare hashes to prevent timing attacks
  return timingSafeEqual(
    Buffer.from(inputHash, "hex"),
    Buffer.from(storedHash, "hex")
  );
}

// Example Usage
const userPassword = "password123";
const { hashedPassword, salt } = hashPassword(userPassword);

// Simulate user input
const inputPassword = "password"; // Change this to test other inputs
if (verifyPassword(inputPassword, hashedPassword, salt)) {
  console.log("Login successful");
} else {
  console.log("Login failed");
}
