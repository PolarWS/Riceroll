<template>
    <div class="loadingDynamicEffect" :style="{ width: loadingSize.width, height: loadingSize.height }">
        <svg :width="loadingSize.size" :height="loadingSize.size" viewBox="0 0 44 44" xmlns="http://www.w3.org/2000/svg"
            stroke="#fff">
            <g fill="none" fill-rule="evenodd" stroke-width="2">
                <circle cx="22" cy="22" r="1">
                    <animate attributeName="r" begin="0s" dur="1.8s" values="1; 20" calcMode="spline" keyTimes="0; 1"
                        keySplines="0.165, 0.84, 0.44, 1" repeatCount="indefinite" />
                    <animate attributeName="stroke-opacity" begin="0s" dur="1.8s" values="1; 0" calcMode="spline"
                        keyTimes="0; 1" keySplines="0.3, 0.61, 0.355, 1" repeatCount="indefinite" />
                </circle>
                <circle cx="22" cy="22" r="1">
                    <animate attributeName="r" begin="-0.9s" dur="1.8s" values="1; 20" calcMode="spline" keyTimes="0; 1"
                        keySplines="0.165, 0.84, 0.44, 1" repeatCount="indefinite" />
                    <animate attributeName="stroke-opacity" begin="-0.9s" dur="1.8s" values="1; 0" calcMode="spline"
                        keyTimes="0; 1" keySplines="0.3, 0.61, 0.355, 1" repeatCount="indefinite" />
                </circle>
            </g>
        </svg>
    </div>
</template>
<script>
export default {
    props: {
        loadingSize: {
            type: Object,
            default: () => ({
                size: 75,
                width: "100%",
                height: "20rem",
            })
        }
    },
}
</script>
<style>
.loadingDynamicEffect {
    display: flex;
    justify-content: center;
    align-items: center;
}

.loadingDynamicEffect svg {
    stroke: var(--color-theme-blue-1);
}
</style>