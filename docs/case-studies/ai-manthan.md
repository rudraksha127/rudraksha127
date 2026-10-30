# AI MANTHAN 2.0 — Event Platform & Progressive Web App

> Status: Public project repository with an event website  
> Repository: [rudraksha127/AI-MANTHAN-2K26](https://github.com/rudraksha127/AI-MANTHAN-2K26)  
> Project site: [nex-ai.in](https://www.nex-ai.in)

## Problem space

An event platform must make schedules, challenge tracks, people, venue information, and support workflows easy to access on mobile devices. It should also degrade gracefully when a participant has intermittent connectivity.

## Repository-documented scope

The project README describes a Next.js App Router application with:

- Installable PWA support through a web app manifest and platform-specific install guidance.
- A service worker for app-shell/core-asset caching and an offline fallback route.
- An IndexedDB-backed queue for support inquiries, with synchronization when connectivity returns.
- Content-driven routes for people, challenge statements, organising teams, and support information.
- Responsive visual components, a countdown, and event timeline interactions.
- Deployment configuration and security-header configuration in the frontend application.

The repository documents Next.js 16, React 19, and Tailwind CSS v4. Re-check package manifests before quoting exact versions in future updates.

## Architecture sketch

~~~mermaid
flowchart TD
    U[Participant / Visitor] --> P[Next.js PWA]
    P --> R[App Router and page components]
    P --> M[Manifest and install experience]
    P --> SW[Service worker]
    SW --> C[Cached app shell and core assets]
    P --> O[Offline fallback]
    P --> Q[Support workflow]
    Q --> IDB[(IndexedDB action queue)]
    IDB --> SYNC[Reconnect and synchronization]
~~~

This is a conceptual view of the components documented in the repository, not a deployment topology or a claim about backend infrastructure.

## Engineering considerations

- **Offline behaviour:** decide which pages/assets are safe to cache and which user actions must be queued rather than silently discarded.
- **User feedback:** distinguish an action saved locally from an action successfully delivered to a remote service.
- **PWA lifecycle:** account for install prompts, service-worker updates, cache invalidation, and browser differences.
- **Data handling:** define what is queued, how retries work, and how duplicate submissions are prevented.
- **Security:** keep secrets out of the client bundle and validate any support submission on the server-side service that receives it.

## Verification

The repository includes its own setup, production build, deployment, and security-policy instructions. This profile update did not execute the application build or an end-to-end browser test. For current verification, follow the repository's installation steps, run its production build, and test the offline/online transition on the target browsers.

## Attribution and next evidence to add

Before using this project as a personal ownership example in an interview, document the exact personal contribution, team responsibilities, and code areas personally implemented. Add a dated build result and a short screen recording or screenshots of install, offline fallback, queued support, and reconnect behaviour.
