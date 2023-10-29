const { toggleMenu, closeMenu } = require('../script.js'); 
test('toggleMenu should toggle the menu', () => {
    const menuContainer = { style: { left: '0px' } };
    const overlay = { style: { width: '100%' } };

    toggleMenu(menuContainer, overlay);

    expect(menuContainer.style.left).toBe('-250px');
    expect(overlay.style.width).toBe('0');
});

test('closeMenu should close the menu', () => {
    const menuContainer = { style: { left: '0px' } };
    const overlay = { style: { width: '100%' } };

    closeMenu(menuContainer, overlay);

    expect(menuContainer.style.left).toBe('-250px');
    expect(overlay.style.width).toBe('0');
});
