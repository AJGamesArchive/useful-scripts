// Check a given string for special characters, returns true or false
function specialCharsCheck(str: string) {
  const specialChars = /[`!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~]/
  return specialChars.test(str)
}