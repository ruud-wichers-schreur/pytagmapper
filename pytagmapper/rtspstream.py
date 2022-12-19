import cv2

# RTSP stream URL
stream_url = "rtsp://@192.168.178.241/live0"

# Create a VideoCapture object
cap = cv2.VideoCapture(stream_url)

# Check if the stream is opened
if not cap.isOpened():
    print("Error opening the debugstream. Check if the URL is correct")

# Read the frames from the stream
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Error reading the frame")
        break

    # Display the frame
    cv2.imshow('Frame', frame)

    # Press q to stop the stream
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()