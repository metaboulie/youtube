<!-- src/routes/ChannelIntro.svelte -->
<script lang="ts">
    let show = false;
    import { onMount } from 'svelte';
  
    onMount(() => {
      show = true;  // Trigger animation on mount
    });
  </script>
  
  <div class="flex items-center justify-center h-screen bg-black">
    {#if show}
      <h1
        class="text-6xl font-bold text-white animate-fade-scale"
      >
        deepBoredom
      </h1>
    {/if}
  </div>
  