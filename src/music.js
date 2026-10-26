/** Original piano miniature, enabled by default; respect browser autoplay gates. */
export function startGardenMusic(button){
  const music=document.createElement('audio');
  music.src=import.meta.env.BASE_URL+'audio/garden-piano.mp3';
  music.loop=true;music.autoplay=true;music.preload='auto';music.volume=.32;
  music.id='garden-music';music.setAttribute('aria-label','A Garden Between Words — gentle piano');
  document.body.append(music);
  let enabled=true;
  try{enabled=localStorage.getItem('bloombound.music')!=='off';}catch{}
  function paint(){const playing=!music.paused;button.textContent=enabled?'♫':'♪';button.setAttribute('aria-pressed',String(enabled));button.setAttribute('aria-label',enabled?'Mute garden music':'Enable garden music');button.title=enabled?(playing?'Gentle piano · on':'Music enabled · starts with your first interaction'):'Music off';button.dataset.playback=playing?'playing':enabled?'waiting':'muted';}
  async function play(){if(!enabled||document.hidden)return;try{await music.play();}catch{}paint();}
  button.onclick=()=>{enabled=!enabled;try{localStorage.setItem('bloombound.music',enabled?'on':'off');}catch{}if(enabled)play();else music.pause();paint();};
  const unlock=e=>{if(e.target.closest?.('#sound'))return;play();};
  document.addEventListener('pointerdown',unlock,{passive:true});
  document.addEventListener('keydown',unlock);
  document.addEventListener('visibilitychange',()=>{if(document.hidden)music.pause();else play();});
  music.addEventListener('playing',paint);music.addEventListener('pause',paint);music.addEventListener('error',()=>{button.title='Music could not load. Tap to try again.';});
  if(!enabled){music.autoplay=false;music.pause();}
  paint();play();
  return {celebrate(){/* The piano remains uninterrupted during play. */}};
}
