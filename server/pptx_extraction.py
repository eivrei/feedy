from pptx import Presentation

def extract(filename):
    # Generates a list on the form [[title, point, point, ...], [title, point, point, ...], ...]
    prs = Presentation('./temp/' + filename)
    all_data = []
    for slide in prs.slides:
        slide_data = []
        for shape in slide.shapes:
            sub_points = []
            last_level = 0
            if not shape.has_text_frame:
                continue
            for paragraph in shape.text_frame.paragraphs:
                for run in paragraph.runs:
                    # If point is subpoint -> make new question with subpoints as points
                    if paragraph.level > last_level and paragraph.level == 1:
                        sub_points.extend([slide_data[-1], run.text])
                    elif paragraph.level == 1:
                        sub_points.append(run.text)
                    elif paragraph.level < last_level:
                        all_data.append(sub_points)
                        slide_data.append(run.text)
                        sub_points = []
                    else:
                        slide_data.append(run.text)
                    last_level = paragraph.level
        all_data.append(slide_data)
    return all_data
