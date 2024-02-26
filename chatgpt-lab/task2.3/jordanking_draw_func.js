// Acts as a loop that draws multiple short lines to give off the impression of drawing.
function draw(e) {
  // Prevents the user from drawing if pen isn't touching pad.
  if (!painting) return;

  // Destructure data from the event object and calculate offsets.
  const { clientX, clientY, pressure } = e;
  const offsetX = canvas.offsetLeft + 2;
  const offsetY = canvas.offsetTop + 2;

  // Gets accurate position of pen.
  const xPos = clientX - offsetX;
  const yPos = clientY - offsetY;

  // Set the visual data for the pen stroke.
  ctx.lineWidth = pressure * 5;
  ctx.lineCap = "round";
  ctx.strokeStyle = "#000000";

  // Draw the line.
  ctx.lineTo(xPos, yPos);
  ctx.stroke();
  ctx.beginPath();
  ctx.moveTo(xPos, yPos);

  // Calculate the total distance travelled (will be used in velocity calculation).
  const PIXEL_TO_METER_SCALAR = 0.0002645833;
  totalDistance += Math.hypot(xPos - lastX, yPos - lastY) * PIXEL_TO_METER_SCALAR; 
  lastX = xPos;
  lastY = yPos;
}
