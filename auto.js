async function sendAttendanceToGitHub(attendanceData) {
  try {
    // Generate unique filename based on timestamp
    const timestamp = new Date().toISOString().replace(/[:\.]/g, '-');
    const filename = `emergency-attendance-${timestamp}.json`;
    
    // Convert data to Base64 (required by GitHub API)
    const content = btoa(JSON.stringify(attendanceData));
    
    // GitHub API request to create the file
    const response = await fetch(
      `https://api.github.com/repos/Chan041103/test-repo/contents/emergency/${filename}`,
      {
        method: 'PUT',
        headers: {
          'Authorization': `Bearer ${GITHUB_TOKEN}`,
          'Accept': 'application/vnd.github+json',
          'X-GitHub-Api-Version': '2022-11-28',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          message: `Emergency attendance record - ${timestamp}`,
          content: content,
          branch: 'main'
        })
      }
    );
    
    const result = await response.json();
    console.log(`Attendance recorded successfully: ${filename}`);
    return result;
  } catch (error) {
    console.error('Failed to send attendance to GitHub:', error);
    // Store in fallback system
    storeInBackupSystem(attendanceData);
    throw error;
  }
}
