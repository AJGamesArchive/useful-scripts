// Create string with current date and time in DD/MM/YYYY - HH/MM
function dateTime() {
  const today = new Date()
  const date: string = String(today.getDate()).padStart(2, "0") + "/" + String(today.getMonth() + 1).padStart(2, "0") + "/" + today.getFullYear() + " - " + String(today.getHours()).padStart(2, "0") + ":" + String(today.getMinutes()).padStart(2, "0")
  return date;
}