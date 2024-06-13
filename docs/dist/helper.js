function type(element, text) {
    if (!element.typed) {
        element.typed = new Typed(element, {
            strings: [text],
            typeSpeed: 50,
            onComplete: (self) => {
                const completeEvent = new Event('typeComplete', {bubbles: true});
                element.dispatchEvent(completeEvent);
            }
        });
    }
}

function createTooltip(element, text) {
    tippy(element, {
        content: text
    });
}