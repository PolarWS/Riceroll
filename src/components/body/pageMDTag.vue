<template>
    <div id="pageMDTag" v-show="markDownDataTag.length">
        <div id="pageMDTagIcon">
            <svg t="1702357041377" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
                p-id="4240" width="15" height="15">
                <path
                    d="M995.126867 592.38l-360.08 360.08a53.333333 53.333333 0 0 1-71.333334 3.68l356.22-356.22a64 64 0 0 0 0-90.506667L495.8402 85.333333h45.573333a52.986667 52.986667 0 0 1 37.713334 15.62l416 416a53.4 53.4 0 0 1 0 75.426667z m-128 0l-360.08 360.08a53.333333 53.333333 0 0 1-75.426667 0l-416-416A52.986667 52.986667 0 0 1 0.0002 498.746667V138.666667a53.393333 53.393333 0 0 1 53.333333-53.333334h360.08a52.986667 52.986667 0 0 1 37.713334 15.62l416 416a53.4 53.4 0 0 1 0 75.426667zM341.333533 341.333333a85.333333 85.333333 0 1 0-85.333333 85.333334 85.426667 85.426667 0 0 0 85.333333-85.333334z"
                    fill="#8f8f8f" p-id="4241"></path>
            </svg>
        </div>
        <div id="pageMDTagItemBox">
            <span class="pageMDTagItem" v-for="item in markDownDataTag" @click="labelQuery(item)">{{ item }}</span>
        </div>
    </div>
</template>
<script>
export default {
    props: {
        markDownDataTag: {
            type: Array,
            default: () => [],
        }
    },
    methods: {
        labelQuery(tag) {
            this.$router.push({ path: '/filePage', query: { sortOrder: "tag", content: tag } });
        }
    },
}
</script>
<style scoped>
#pageMDTag {
    display: flex;
    padding: 0.5rem 1.5rem 2rem 1.5rem;
}

#pageMDTagIcon {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 2rem;
    height: 2rem;
}

#pageMDTagItemBox {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    margin-left: 1rem;
    gap: 1rem;
}

.pageMDTagItem {
    font-size: 0.75rem;
    color: var(--color-theme-grayscale5);
    padding: 0.5rem 1rem;
    border-radius: 0.5rem;
    background-color: var(--color-theme-grayscale1);
    cursor: pointer;
    transition: color 0.15s, background-color 0.15s;
}

.pageMDTagItem:hover {
    color: var(--color-theme-grayscale1);
    background-color: var(--color-theme-grayscale5);
}
</style>