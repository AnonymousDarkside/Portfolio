            <div class="profile-container">
              <img
                src="assests\Home\profile.jpg"
                alt="Satyam Kumar Profile Picture"
              />
              <div class="profile-decoration"></div>
            </div>

.profile-decoration {
  position: absolute;
  top: -10px;
  right: -10px;
  width: 60px;
  height: 60px;
  background: var(--secondary-color);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  box-shadow: 0 4px 15px rgba(80, 227, 194, 0.5);
}

.profile-decoration::after {
  content: '💡';
}




      <section id="recent-activity" class="recent-activity-section">
        <div class="container">
          <h2>Recent Activity</h2>
          <div class="activity-grid">
            <div class="activity-item">
              <div class="activity-icon">📝</div>
              <div class="activity-content">
                <h4>Latest Blog Post</h4>
                <p>
                  DIY Ambilight TV Backlight - Creating an immersive viewing
                  experience
                </p>
                <span class="activity-date">Recently Updated</span>
              </div>
            </div>
            <div class="activity-item">
              <div class="activity-icon">🏆</div>
              <div class="activity-content">
                <h4>Project Milestone</h4>
                <p>
                  Successfully deployed Home Assistant with 15+ integrated
                  devices
                </p>
                <span class="activity-date">This Month</span>
              </div>
            </div>
            <div class="activity-item">
              <div class="activity-icon">🔧</div>
              <div class="activity-content">
                <h4>New Technology</h4>
                <p>
                  Exploring local LLM deployment for privacy-focused AI
                  solutions
                </p>
                <span class="activity-date">In Progress</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section id="cta" class="cta-section">
        <div class="container">
          <div class="cta-content">
            <h2>Let's Build Something Amazing Together</h2>
            <p>
              I'm always excited to collaborate on innovative projects,
              especially those involving IoT, automation, or creative technology
              solutions. Whether you have an idea or want to discuss potential
              opportunities, I'd love to hear from you.
            </p>
            <div class="cta-buttons">
              <a href="contact.html" class="btn btn-primary">Get In Touch</a>
              <a
                href="assests/Resume v2.1.pdf"
                class="btn btn-secondary"
                target="_blank"
                download
                >Download Resume</a
              >



