const hideShowCard = () => {
    const displayedCards = document.querySelectorAll('[data-name=hero]');
    const detailCards = document.querySelectorAll('[data-name=detail]');
    displayedCards.forEach(card => {
        card.addEventListener('click', event => {
            const currentCard = event.currentTarget;
            const currentMarket = currentCard.dataset.market;
            const detailCard = document.querySelector(`[data-market='${currentMarket}'][data-name=detail]`);
            detailCard.style.display = 'block';
            currentCard.style.display = 'none';
        });
    });
    detailCards.forEach(card => {
        card.addEventListener('click', event => {
            const currentCard = event.currentTarget;
            const currentMarket = currentCard.dataset.market;
            const heroCard = document.querySelector(`[data-market='${currentMarket}'][data-name=hero]`);
            heroCard.style.display = 'flex';
            currentCard.style.cssText = 'display: none !important';
        });
    });
}

document.addEventListener('DOMContentLoaded', () => hideShowCard());
