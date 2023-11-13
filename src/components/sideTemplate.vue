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
    background-color: var(--color-theme-grayscale1);
    margin: 0 1.5rem 1rem 1.5rem;
    padding: 0.75rem 1.5rem 1.5rem 1.5rem;
    border-radius: 0.75rem;

    transition: transform 0.25s, box-shadow 0.25s;
}

.announcementBoard a {
    text-decoration: none;
    color: var(--color-theme-grayscale5);
    cursor: pointer;
}

.announcementBoard a:hover {
    color: var(--color-theme-grayscale6);
}

.announcementBoard a:active {
    color: var(--color-theme-blue-2);
}

.announcementBoard:hover {
    box-shadow: 0 0 0.5rem var(--color-theme-grayscale3);
    transform: translateY(-0.2rem);
}


.announcementBoard span {
    color: var(--color-theme-grayscale5);
}

.announcementBoardTitleContent {
    margin: 0.5rem;
}
</style>