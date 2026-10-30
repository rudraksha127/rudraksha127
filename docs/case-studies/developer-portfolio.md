# Developer Portfolio — Interactive Website

> Status: Public source repository  
> Repository: [rudraksha127/Portfolio](https://github.com/rudraksha127/Portfolio)

## Purpose

A personal portfolio website provides a structured way to present projects, skills, education, experience, credentials, and contact information. The codebase explores a modular React/Next.js implementation with a space-inspired visual system.

## Repository-documented stack

- Next.js 16 and React 19.
- TypeScript and Tailwind CSS.
- Framer Motion for transitions and motion effects.
- Three.js and React Three Fiber/Drei for the 3D visual layer.
- Modular components for hero, about, experience, education, skills, projects, certifications, and contact.

Exact dependency versions should be taken from the current package manifest, not copied from an older README.

## Contribution and attribution

The public history includes a portfolio-theme pull request merged under @rudraksha127, while several implementation commits in that history are authored by Claude. This case study therefore describes the repository's architecture and design, not a claim that every implementation line was independently authored. Present personal work as requirements/design direction, review, integration, or specific code changes only where you can point to the corresponding commit or pull request and explain it.

## Design and implementation considerations

- Keep content separate from presentation where practical.
- Build reusable section and project-card components.
- Ensure the visual system works at mobile, tablet, and desktop widths.
- Respect reduced-motion preferences and avoid making animation a requirement for understanding content.
- Provide accessible labels, semantic structure, keyboard interaction, and clear form states.
- Lazy-load or defer expensive visual assets where appropriate.
- Keep external links and resume downloads valid and current.

## Verification and known boundary

The profile links to the repository source. It does not link to a live deployment because a production URL was not independently established during this profile update. Performance figures and Lighthouse targets in the project README are not presented as measured results here.

## Next evidence to add

Add screenshots from the actual current build, a current production deployment URL if available, an accessibility audit, responsive test notes, and measured Core Web Vitals or Lighthouse results with the date and test environment.
