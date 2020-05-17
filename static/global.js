const showDetails = (event, isDetail=false) => {
  const currentCard = event;
  const currentMarket = currentCard.dataset.market;
  if (isDetail) {
    const detailCard = document.querySelector(`[data-market='${currentMarket}'][data-name=hero]`);
    detailCard.style.display = 'flex';
    currentCard.style.cssText = 'display: none !important';
  } else {
    const detailCard = document.querySelector(`[data-market='${currentMarket}'][data-name=detail]`);
    detailCard.style.display = 'block';
    currentCard.style.display = 'none';
  }
}
