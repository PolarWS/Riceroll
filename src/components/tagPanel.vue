<template>
    <div id="tagPanel" v-show="tagData.length">
        <div id="tagPanelIcon">
            <svg t="1715829563575" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
                p-id="4284" width="15" height="15">
                <path
                    d="M867.126867 516.953333l-416-416A52.986667 52.986667 0 0 0 413.413533 85.333333H53.333533a53.393333 53.393333 0 0 0-53.333333 53.333334v360.08a52.986667 52.986667 0 0 0 15.62 37.713333l416 416a53.333333 53.333333 0 0 0 75.426667 0l360.08-360.08a53.4 53.4 0 0 0 0-75.426667zM341.333533 341.333333a85.333333 85.333333 0 1 1-85.333333-85.333333 85.426667 85.426667 0 0 1 85.333333 85.333333z m653.793334 251.046667l-382.706667 382.706667a21.333333 21.333333 0 0 1-30.173333-30.173334l382.706666-382.706666a10.666667 10.666667 0 0 0 0-15.08L539.5802 121.753333a21.333333 21.333333 0 0 1 30.173333-30.173333l425.373334 425.373333a53.4 53.4 0 0 1 0 75.426667z"
                    fill="#8f8f8f" p-id="4285"></path>
            </svg>
        </div>
        <div id="tagPanelItemBox">
            <span class="tagPanelItem" v-for="item in tagData" @click="labelSearch(item)">{{ item }}</span>
        </div>
    </div>
</template>
<script>
export default {
    props: {
        tagData: {
            type: Array,
            default: () => [],
        }
    },
    methods: {
        labelSearch(tag) {
            this.$router.push({ path: '/filePage', query: { class: "tag", content: tag } });
        },
    },
}
</script>
<style scoped>
#tagPanel {
    display: flex;
    padding: 1.5rem;
}

#tagPanelIcon {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 2rem;
    height: 2rem;
}

#tagPanelItemBox {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    margin-left: 1rem;
    gap: 1rem;
}

.tagPanelItem {
    font-size: 0.75rem;
    color: var(--color-theme-grayscale5);
    padding: 0.5rem 1rem;
    border-radius: 0.5rem;
    background-color: var(--color-theme-grayscale1);
    cursor: pointer;
    transition: color 0.15s, background-color 0.15s;
}

.tagPanelItem:hover {
    color: var(--color-theme-grayscale1);
    background-color: var(--color-theme-grayscale5);
}

@media screen and (max-width: 600px) {
    #tagPanel {
        padding: 0.5rem 1.15rem 2rem 1.15rem;
    }
}
</style>