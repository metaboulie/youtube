<script lang="ts">
    export let sectionTitle: string;
    export let sectionDescription: string;
    let visible = false;
    let zoomOut = false;
  
    // Delay animation start by 2 seconds
    setTimeout(() => (visible = true), 2000);

    // Zoom out the content after 5 seconds
    setTimeout(() => (zoomOut = true), 5000);
</script>

<div class={`flex flex-col items-center justify-center h-screen bg-nord-bg-warp ${zoomOut ? 'animate-zoom-out' : ''}`}>
    {#if visible}
        <h1 class="text-7xl font-font-title text-nord-frost-2 mb-6 animate-fade-fly-up tracking-widest font-thin">
            {sectionTitle}
        </h1>

        <h2 class="text-xl font-font-header text-nord-frost-1 animate-fade-fly-down tracking-wide font-light mt-2 lowercase">
            {sectionDescription}
        </h2>
    {/if}
</div>