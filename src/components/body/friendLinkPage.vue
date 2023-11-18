<template>
    <div id="pressed" :style="cardBoxAdaptation.grid">
        <div class="cardBox" v-for="(item, index) in itemData.cardList" @click="linkClick(item.url)">
            <div class="cardImg">
                <img :src="(item.src)" />
                <div class="state" :class="statePing(this.pingData[index])"></div>
            </div>
            <div class="cardContent">
                <div class="title" :style="cardBoxAdaptation.width">{{ item.title }}</div>
                <span class="content" :style="cardBoxAdaptation.width">{{ item.content }}</span>
            </div>
        </div>
    </div>
</template>

<script>
import { useCounterStore } from '../../store/axiosStore.js';
export default {
    data() {
        return {
            pingData: Object,
            cardBoxAdaptation: {
                'grid': {
                    'grid-template-columns': '',
                },
                'width': {
                    width: '',
                },
            },
        }
    },
    methods: {
        linkClick(url) {
            window.open(url);
        },
        statePing(delay) {
            if (delay < 50) {
                return "stateG";
            } else if (delay < 200) {
                return "stateY";
            } else if (delay < 998) {
                return "stateO";
            } else {
                return "stateR";
            }
        },
        checkWidth() {
            const element = document.querySelector('#pressed');
            if (element.offsetWidth < 600) {
                this.cardBoxAdaptation.grid['grid-template-columns'] = '1fr';
                this.cardBoxAdaptation.width.width = '10rem';
            } else {
                this.cardBoxAdaptation.grid['grid-template-columns'] = 'repeat(2, 1fr)';
                this.cardBoxAdaptation.width.width = '9rem';
            }
        },
    }, mounted() {
        this.checkWidth();
        window.addEventListener('resize', this.checkWidth);
    }, created() {
        useCounterStore().apiRequest(this.api.url + this.api.frindLinkPage).then(data => {
            if (data.status == 200) {
                this.pingData = data.ping;
            }
        });
    }, unmounted() {
        // 在组件销毁前移除事件监听器
        window.removeEventListener('resize', this.checkWidth);
    }, props: {
        itemData: Object,
    }, inject: ['api'],
}
</script>
<style scoped>
.content {
    width: 9rem;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;
    -webkit-line-clamp: 2;
}

.title {
    font-size: 1.35rem;
    font-weight: 520;
    margin-top: 0;
    margin-bottom: 0.5rem;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.state {
    width: 0.85rem;
    height: 0.85rem;
    border-radius: 50%;
    border: 0.25rem solid var(--color-theme-white);
    position: absolute;
    margin-top: 5rem;
}

.stateG {
    background-color: var(--color-theme-G);
}

.stateY {
    background-color: var(--color-theme-Y);
}

.stateO {
    background-color: var(--color-theme-O);
}

.stateR {
    background-color: var(--color-theme-R);
}

.content {
    color: #8A8E90;
}

#pressed {
    display: grid;
    gap: 1rem;
    margin: 1.5rem;
}

.cardBox {
    display: grid;
    border-radius: 0.55rem;
    height: 9.5rem;
    grid-template-columns: 2fr 3fr;
    justify-content: center;
    border: 2px solid var(--color-theme-grayscale1);
    cursor: pointer;

    transition: box-shadow 0.25s;
}

.cardBox:hover {
    box-shadow: 0 0 0.5rem 0.02rem var(--color-theme-grayscale2);
}

.cardBox img {
    width: 6rem;
    height: 6rem;
    object-fit: cover;
    border-radius: 50%;
}

.cardContent {
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 1rem;
}

.cardImg {
    display: flex;
    align-items: center;
    justify-content: right;
}
</style>
