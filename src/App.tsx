// Placeholder title screen — just proves the environment works.
// Real screens (character select, date scenes, dialogue) come with the full brief.
export default function App() {
  return (
    <main className="title-screen">
      <div className="hearts" aria-hidden="true">
        {Array.from({ length: 14 }, (_, i) => (
          <span key={i} style={{ left: `${(i * 7.3) % 100}%`, animationDelay: `${i * 0.6}s` }}>
            ♥
          </span>
        ))}
      </div>
      <h1 className="logo">
        AI <span>Dating</span> Sim
      </h1>
      <p className="tagline">find love in the latent space</p>
      <button className="start" onClick={() => alert('Coming soon <3')}>
        ♥ Start ♥
      </button>
    </main>
  )
}
