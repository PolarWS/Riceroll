<!-- 侧边栏模板 -->
<template>
    <div class="announcementBoard">
        <div class="announcementBoardTitle">
            <h2>
                <slot name="title">
                </slot>
            </h2>
        </div>
        <div class="announcementBoardTitleContent">
            <slot name="content">
            </slot>
        </div>
    </div>
</template>
<style>
.announcementBoard {
    background-color: #F4F4F4;
    margin: 1rem 1.5rem;
    padding: 0.75rem 1.5rem 1.5rem 1.5rem;
    border-radius: 0.75rem;
}

.announcementBoard a {
    text-decoration: none;
    color: #8A8E90;
    cursor: pointer;
}

.announcementBoard a:hover {
    color: #575757;
}

.announcementBoard a:active {
    color: #74E4FB;
}

.announcementBoard:hover {
    box-shadow: 0 0 0.5rem #e0e0e0;
    animation: floatUp 0.5s ease-in-out forwards;
}


.announcementBoard span {
    color: #8A8E90;
}

.announcementBoardTitleContent {
    margin: 0.5rem;
}

@keyframes floatUp {
    0% {
        transform: translateY(0);
    }

    50% {
        transform: translateY(-0.15rem);
    }

    100% {
        transform: translateY(-0.2rem);
    }
}
</style>