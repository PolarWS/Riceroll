<template>
    <div id="topMenuBarBox">
        <div id="topMenuBarIcon">
            <svg t="1700135227298" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
                p-id="7094" width="30" height="30">
                <path
                    d="M853.333333 218.666667a37.333333 37.333333 0 0 1 3.072 74.538666L853.333333 293.333333H362.666667a37.333333 37.333333 0 0 1-3.072-74.538666L362.666667 218.666667h490.666666zM853.333333 474.666667a37.333333 37.333333 0 0 1 3.072 74.538666L853.333333 549.333333H362.666667a37.333333 37.333333 0 0 1-3.072-74.538666L362.666667 474.666667h490.666666zM853.333333 730.666667a37.333333 37.333333 0 0 1 3.072 74.538666L853.333333 805.333333H362.666667a37.333333 37.333333 0 0 1-3.072-74.538666L362.666667 730.666667h490.666666z"
                    fill="#2c2c2c" p-id="7095"></path>
                <path
                    d="M202.666667 256m-53.333334 0a53.333333 53.333333 0 1 0 106.666667 0 53.333333 53.333333 0 1 0-106.666667 0Z"
                    fill="#2c2c2c" p-id="7096"></path>
                <path
                    d="M202.666667 512m-53.333334 0a53.333333 53.333333 0 1 0 106.666667 0 53.333333 53.333333 0 1 0-106.666667 0Z"
                    fill="#2c2c2c" p-id="7097"></path>
                <path
                    d="M202.666667 768m-53.333334 0a53.333333 53.333333 0 1 0 106.666667 0 53.333333 53.333333 0 1 0-106.666667 0Z"
                    fill="#2c2c2c" p-id="7098"></path>
            </svg>
        </div>
        <h3>鸦鸦的小窝</h3>
    </div>
</template>
<script>
export default {
    data() {
        return {
            scrollY: 0,
        }
    },
    methods: {
        handleScroll() {
            if (window.scrollY > this.scrollY) {
                this.scrollY = window.scrollY;
                document.getElementById("topMenuBarBox").style.top = "-73px";
            } else {
                this.scrollY = window.scrollY;
                document.getElementById("topMenuBarBox").style.top = "0px";
            }
        },
    },
    mounted() {
        window.addEventListener('scroll', this.handleScroll);

    },
    beforeDestroy() {
        window.removeEventListener('scroll', this.handleScroll);
    },
}
</script>
<style scoped>
#topMenuBarBox {
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: fixed;
    z-index: 1;
    top: 0;
    width: 100%;
    height: 3.5rem;
    background-color: var(--color-theme-white-2);
    transition: top 0.3s;
}

#topMenuBarBox h3 {
    margin-right: 1.5rem;
    color: var(--color-theme-icon-1);
}

#topMenuBarIcon {
    margin-left: 0.5rem;
    height: 100%;
    width: 3.5rem;
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>