<template>
    <div id="topMenuBarBox">
        <div id="topMenuBarTitle">
            <div class="topMenuBarIcon" @click="navigationBarMobOpen">
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
            <h3 v-if="searchPageSwitch">{{ blogName }}</h3>
        </div>
        <h3 v-if="!searchPageSwitch">{{ blogName }}</h3>
        <div class="topMenuBarIcon" @click="openSearchPage" v-if="searchPageSwitch">
            <svg t="1698845441753" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
                p-id="23255" width="25" height="25">
                <path
                    d="M953.474215 908.234504l-152.576516-163.241391c61.92508-74.48211 95.81186-167.36973 95.81186-265.073744 0-229.294809-186.63531-415.930119-416.102133-415.930119-229.294809 0-415.930119 186.63531-415.930119 415.930119s186.63531 415.930119 415.930119 415.930119c60.032925 0 118.00168-12.55703 172.186125-37.327062 16.169326-7.396607 23.221905-26.318159 15.825298-42.315471-7.396607-16.169326-26.318159-23.221905-42.315471-15.825298-45.927768 20.813707-94.951789 31.478582-145.695952 31.478582-194.031917 0-351.94087-157.908953-351.94087-351.94087 0-194.031917 157.908953-351.94087 351.94087-351.94087 194.031917 0 351.94087 157.908953 351.94087 351.94087 0 91.339493-34.918864 177.86259-98.048043 243.743995-12.213002 12.729044-11.868974 33.026709 0.860071 45.239711 1.032085 0.860071 2.236183 1.204099 3.268268 2.064169 0.860071 1.204099 1.376113 2.752226 2.408198 3.956325l165.477574 177.00252c6.192508 6.70855 14.793214 10.148833 23.393919 10.148833 7.912649 0 15.653284-2.92424 21.845792-8.600706C964.827146 941.433227 965.515202 921.135562 953.474215 908.234504z"
                    fill="#2c2c2c" p-id="23256"></path>
            </svg>
        </div>
    </div>
</template>
<script>
export default {
    data() {
        return {
            scrollY: 0,
            searchPageSwitch: false,
        }
    },
    methods: {
        navigationBarMobOpen() {
            this.$emit('navigationBarMobSwitch', true);
        },
        openSearchPage() {
            this.$router.push('/searchPage');
        },
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
        for (let i = 0; i < this.navigationBarData.length; i++) {
            if (this.navigationBarData[i].id === 'searchPage') {
                this.searchPageSwitch = true;
            }
        }
    },
    unmounted() {
        window.removeEventListener('scroll', this.handleScroll);
    },
    props: {
        blogName: String,
        navigationBarData: Object,
    },
}
</script>
<style scoped>
#topMenuBarBox {
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: sticky;
    z-index: 1;
    top: 0;
    width: 100%;
    height: 3.5rem;
    background-color: var(--color-theme-white-3);
    transition: top 0.3s;
}

#topMenuBarTitle {
    display: flex;
    align-items: center;
}

#topMenuBarBox h3 {
    margin-right: 1.5rem;
    margin-left: 1rem;
    color: var(--color-theme-icon-1);
}

.topMenuBarIcon {
    margin-left: 0.5rem;
    margin-right: 0.5rem;
    height: 100%;
    width: 3.5rem;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: transform 0.1s;
    cursor: pointer;
}

.topMenuBarIcon:active {
    transform: scale(0.85);
}
</style>