// Documentation Page JavaScript

document.addEventListener('DOMContentLoaded', function() {
    initializeSmoothScrolling();
    initializeActiveSectionHighlighting();
    initializeMobileNavigation();
});

function initializeSmoothScrolling() {
    // Smooth scrolling for sidebar navigation links
    document.querySelectorAll('.sidebar-nav a[href^="#"]').forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                const headerOffset = 100; // Account for sticky nav
                const elementPosition = targetElement.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

function initializeActiveSectionHighlighting() {
    const sections = document.querySelectorAll('.doc-section[id]');
    const navLinks = document.querySelectorAll('.sidebar-nav a');
    
    const observerOptions = {
        threshold: 0.3,
        rootMargin: '-100px 0px -50% 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.getAttribute('id');
                
                // Remove active class from all nav links
                navLinks.forEach(link => link.classList.remove('active-section'));
                
                // Add active class to current section link
                const activeLink = document.querySelector(`.sidebar-nav a[href="#${id}"]`);
                if (activeLink) {
                    activeLink.classList.add('active-section');
                }
            }
        });
    }, observerOptions);

    sections.forEach(section => {
        observer.observe(section);
    });
}

function initializeMobileNavigation() {
    // Add mobile toggle for sidebar (if needed in the future)
    const sidebar = document.querySelector('.docs-sidebar');
    
    // Collapse sidebar on mobile after clicking a link
    if (window.innerWidth <= 768) {
        document.querySelectorAll('.sidebar-nav a').forEach(link => {
            link.addEventListener('click', function() {
                // Could add mobile sidebar collapse logic here
            });
        });
    }
}

// Add CSS for active section highlighting
const style = document.createElement('style');
style.textContent = `
    .sidebar-nav a.active-section {
        background: #f0f4ff;
        color: #667eea;
        font-weight: 600;
        border-left: 3px solid #667eea;
        padding-left: calc(0.75rem - 3px);
    }
    
    .sidebar-nav a.active-section:hover {
        background: #f0f4ff;
        color: #667eea;
    }
`;
document.head.appendChild(style);